for schema_entry in schema:
    column = schema_entry["name"]
    expected_data_type = schema_entry["type"]
    actual_data_type = df_reorder[column].dtype
    if expected_data_type != actual_data_type:
        print(f"Column '{column}' has an unexpected data type. Expected: {expected_data_type}, Actual: {actual_data_type}")
        # If the data types don't match, you can add conversion logic here.