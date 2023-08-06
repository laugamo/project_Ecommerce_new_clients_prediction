import hydra
from components.data_loading import load_data
from omegaconf import DictConfig


@hydra.main(config_path="../config", config_name="config", version_base=None)
def main(config: DictConfig):
    # Load data
    loaded_data = load_data(config=config.data)

    for file_name, data_frame in loaded_data.items():
        print(f"Data frame for file: {file_name:}")
        print(data_frame.dtypes)
        print()

    # Clean data
    # clean_data = clean_data(config, loaded_data)


if __name__ == "__main__":
    main()
