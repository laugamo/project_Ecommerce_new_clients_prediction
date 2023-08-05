import hydra
from components.data_loading import load_data


@hydra.main(config_path="../config/data", config_name="data_config", version_base=None)
def main(config):
    loaded_data = load_data(config)

    for data_frame in loaded_data:
        print(data_frame.dtypes)
        print()


if __name__ == "__main__":
    main()
