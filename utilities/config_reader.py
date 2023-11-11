import configparser
import os


def read_config(section, key):
    config = configparser.ConfigParser()
    config_path = os.path.join(os.path.dirname(__file__), "../config/configs.cfg")
    print(config_path)
    config.read(config_path)
    return config.get(section,key)

def get_data(section, key):
    config = configparser.ConfigParser()
    config_path = os.path.join(os.path.dirname(__file__), "../config/data.cfg")
    print(config_path)
    config.read(config_path)
    return config.get(section,key)
