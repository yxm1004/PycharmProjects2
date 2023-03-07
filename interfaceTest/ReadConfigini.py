import configparser


def read_config_file(file_path):
    config = configparser.ConfigParser()
    config.read(file_path)
    return config
