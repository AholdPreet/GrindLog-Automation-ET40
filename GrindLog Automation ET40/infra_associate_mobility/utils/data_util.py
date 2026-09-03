import json
import os

class DataUtil:

    @staticmethod
    def load_json(json_file_path):
        with open(json_file_path, "r", encoding="utf-8") as file:
            return json.load(file)