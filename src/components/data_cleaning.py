def remove_duplicates(config, data_frame):
    return data_frame


def clean_data(config, loaded_data):
    # Eliminate duplicates
    for file_name, data_frame in loaded_data.items():
        # Remove duplicates
        loaded_data[file_name] = remove_duplicates(config, data_frame)

        # Correct missleading data

        return loaded_data
