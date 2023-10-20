from flask import Flask, render_template, abort, request
from google.cloud import bigquery
import pandas as pd
import re
import constants
from utils_project import get_prior_file_name, read_excel, get_dest_table

app = Flask(__name__)

client = bigquery.Client(project=constants.PROJECT)


def files_list():
    
    ds_file_list = []
    non_ds_file_list = []
    
    data = client.query(f"""
    SELECT distinct file_name
    FROM
    (
      SELECT file_name, is_active FROM {constants.PIPELINE_TARGET_TABLE_ID}
    ) combined_tables
 
    where is_active = true
    """)



    ds_file_list = [row['file_name'] for row in data]

 
    data = client.query(f"""
    SELECT distinct file_name
    FROM
    (
      SELECT file_name, is_active FROM {constants.CE_TABLE_ID}
      UNION ALL
      SELECT file_name, is_active FROM {constants.MQC_TABLE_ID}
    ) combined_tables
 
    where is_active = true
    """)
    
    non_ds_file_list = [row['file_name'] for row in data]
 
    return ds_file_list, non_ds_file_list


def refresh_df_file_version():

    df_file_name_ds = []
    df_file_name_non_ds = []

    data = client.query(f"""
    SELECT distinct file_name
    FROM
    (
      SELECT file_name, is_active FROM {constants.PIPELINE_TARGET_TABLE_ID}
    ) 
 
    where is_active = true
    """).to_dataframe()

    df_file_name_ds = data

    df_file_name_ds['file_name'] = df_file_name_ds['file_name'].str.replace(".xlsx", "")
    df_file_name_ds['version'] = df_file_name_ds['file_name'].str.split().str[-1]
    df_file_name_ds['file_name'] = df_file_name_ds['file_name'].str.rsplit(n=1).str[0].str.strip()

    data = client.query(f"""
    SELECT distinct file_name
    FROM
    (
      SELECT file_name, is_active FROM {constants.CE_TABLE_ID}
      UNION ALL
      SELECT file_name, is_active FROM {constants.MQC_TABLE_ID}
    ) combined_tables
 
    where is_active = true
    """).to_dataframe()

    df_file_name_non_ds = data

    df_file_name_non_ds['file_name'] = df_file_name_non_ds['file_name'].str.replace(".xlsx", "")
    df_file_name_non_ds['version'] = df_file_name_non_ds['file_name'].str.split().str[-1]
    df_file_name_non_ds['file_name'] = df_file_name_non_ds['file_name'].str.rsplit(n=1).str[0].str.strip()

    return df_file_name_ds, df_file_name_non_ds


def set_false_all_ds(file_name):
    for table in constants.DS_TABLES:
        data = client.query(f""" update {table}
                          set is_active = false
                          where file_name = "{file_name}" """)

def set_false_all_non_ds(file_name):
    for table in constants.NON_DS_TABLES:
        data = client.query(f""" update {table}
                          set is_active = false
                          where file_name = "{file_name}" """)
        

def qc(df):
    pass


def generic_insert_database(df, file_name, table_id, columns_to_keep):
    
    dest_table = get_dest_table(table_id)
    df_reorder = df[columns_to_keep]
    

    table_csw = client.get_table(table_id)
    
    schema = [{"name": field.name, "type": field.field_type} for field in table_csw.schema]

    df_reorder['file_name'] = file_name
    df_reorder['is_active'] = True

    df_reorder.columns = [i.name for i in table_csw.schema]

    df_reorder.to_gbq(destination_table=dest_table, project_id=constants.PROJECT, if_exists="append", table_schema=schema)


@app.route("/", methods=['GET', "POST"])
def home():

    if request.method == "POST":

        if request.form['submit'] == 'Upload Demand Studio':

            file = request.files['file']

            # df_calculated = read_excel(file, "Calculated", constants.COLUMNS_CALCULATED)
            df_pipeline = read_excel(file, "Pipeline", constants.COLUMNS_PIPELINE_TARGET)

            # generic_insert_database(df_calculated, file.filename, constants.CALCULATED_TABLE_ID, constants.COLUMNS_CALCULATED)
            generic_insert_database(df_pipeline, file.filename, constants.PIPELINE_TARGET_TABLE_ID, constants.COLUMNS_PIPELINE_TARGET)

            return render_template("success.html")


        if request.form['submit'] == 'Upload Non Demand Studio':
            
            file = request.files['file2']
            df_CE = read_excel(file, "CE", constants.COLUMNS_CE)
            df_MQC = read_excel(file, "MQC", constants.COLUMNS_MQC)
            generic_insert_database(df_CE, file.filename, constants.CE_TABLE_ID, constants.COLUMNS_CE)
            generic_insert_database(df_MQC, file.filename, constants.MQC_TABLE_ID, constants.COLUMNS_MQC)

            return render_template("success.html")


        if request.form['submit'] == 'delete_ds':
            file_name = request.form['delete_ds']
            set_false_all_ds(file_name)
        
        if request.form['submit'] == 'delete_non_ds':
            file_name = request.form['delete_non_ds']
            set_false_all_non_ds(file_name)


    ds_file_list, non_ds_file_list = files_list()
    ds_file_version, non_ds_file_version = refresh_df_file_version()


    return render_template("index.html", ds_file_list=ds_file_list, non_ds_file_list=non_ds_file_list, 
                           ds_file_version=ds_file_version, non_ds_file_version=non_ds_file_version)


