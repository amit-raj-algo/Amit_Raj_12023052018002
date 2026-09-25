import configparser
import os


class ConfigReader:

    def __init__(self):
        self.config = configparser.ConfigParser()

        base_dir = os.path.dirname(
            os.path.dirname(os.path.abspath(__file__))
        )

        config_path = os.path.join(
            base_dir,
            "config",
            "config.ini"
        )

        self.config.read(config_path)

    def get_application_url(self):
        return self.config["application"]["url"]

    def get_browser(self):
        return self.config["application"]["browser"]