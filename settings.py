# -*- This python file uses the following encoding : utf-8 -*-

import os
import json

class Settings:

    working_directory = os.getcwd()
    json_file = "settings.json"

    settings_path = os.path.join(working_directory, json_file)

    if not os.path.isfile(settings_path):
        print(f"WARNING: \"settings.json\" not found! check in the folder {settings_path}")

    def __init__(self):
        # Settings clone object
        self.items = {}
        self.deserialize()

    def serialize(self):
        """
        Write JSON file
        """
        with open(self.settings_path, "w") as file:
            json.dump(self.items, file, indent=4)

    def deserialize(self):
        """
        Read JSON file
        """
        with open(self.settings_path, "r") as file:
            self.items = json.loads(file.read())


if __name__ == "__main__":
    settings = Settings()
    settings.deserialize()
    settings.serialize()