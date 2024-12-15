import os
import json
import csv
from .core import Variable, VariableManager

class EnvVariableImporter:
    def import_variables(self, manager: VariableManager):
        for name, value in os.environ.items():
            manager.add_variable(Variable(name=name, value=value, description="Variable '{name}' imported from environment"))

class JsonVariableImporter:
    def __init__(self, json_path: str):
        self.json_path = json_path

    def import_variables(self, manager: VariableManager):
        with open(self.json_path, 'r') as file:
            data = json.load(file)
            for item in data:
                manager.add_variable(Variable(
                    name=item["name"],
                    value=item.get("value"),
                    description=item.get("description", f"{item['name']} from JSON"),
                    value_type=item.get("value_type", "text")
                ))

class CsvVariableImporter:
    def __init__(self, csv_path: str):
        self.csv_path = csv_path

    def import_variables(self, manager: VariableManager):
        with open(self.csv_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                manager.add_variable(Variable(
                    name=row["name"],
                    value=row.get("value", None) or None,
                    description=row.get("description", f"{row['name']} from CSV"),
                    value_type=row.get("value_type", "text")
                ))

class ArgvVariableImporter:
    def import_variables(self, manager: VariableManager):
        import sys
        for arg in sys.argv[1:]:
            if "=" in arg:
                name, value = arg.split("=", 1)
                manager.add_variable(Variable(name=name, value=value, description="Variable '{name}' imported from command-line"))