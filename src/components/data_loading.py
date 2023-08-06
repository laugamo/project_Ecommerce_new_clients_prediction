import pandas as pd


def update_column_type(df, col_types, remove_decimals):
    # Update column types
    for col_name, col_type in col_types.items():
        # Replace decimals before converting
        if col_name in remove_decimals:
            df[col_name] = (
                df[col_name].astype("str").str.replace(r"[,.]00$", "", regex=True)
            )
        # Update column types
        if col_type in ("float", "bool", "str", "int"):
            df[col_name] = df[col_name].astype(col_type)
        elif col_type == "date":
            df[col_name] = pd.to_datetime(df[col_name], dayfirst=True)

    return df


def load_data(config):
    # Access the files_to_upload field from the configuration
    files_to_upload = config.data.files_to_upload

    # Initialize dictionary to store the dataframes
    loaded_data = {}

    # Upload data
    for file_name, file_path in files_to_upload.items():
        print(f"Uploading {file_path}...")
        data = pd.read_csv(file_path, sep=";", encoding="latin-1")

        # Apply column type conversions
        data = update_column_type(
            data,
            col_types=config.data.column_types[file_name],
            remove_decimals=config.data.remove_decimals[file_name],
        )
        loaded_data[file_name] = data

    print("All data has been uploaded")
    return loaded_data


if __name__ == "__main__":
    loaded_data = load_data()
