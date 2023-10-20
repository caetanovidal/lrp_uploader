import pandas as pd
import re
from flask import abort
import constants


def get_prior_file_name(file_name):
    if "v" in file_name:
        match = re.search(r"v(\d+)(?=\xlsx$)", file_name)
        if match:
            version_number = int(match.group(1))
            if version_number > 1:
                prior_version_number = version_number - 1
                prior_file_name = file_name.replace(f"v{version_number}", f"v{prior_version_number}")
            else:
                prior_file_name = file_name
        else:
            prior_file_name = file_name
    else:
        prior_file_name = file_name
    
    return prior_file_name

def read_excel(excel_file, tab_name, columns):
    
    try:
        df = pd.read_excel(excel_file, tab_name, usecols=columns)
    except Exception as E:
        abort(404, description=E)

    return df


def get_dest_table(table_id):
    split = table_id.split('.')
    return split[-1] + "." +  split[-2]