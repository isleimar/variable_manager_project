import sys
import unittest
from unittest.mock import patch
from variable_manager.core import Variable, VariableManager
from variable_manager.importers import EnvVariableImporter, JsonVariableImporter, CsvVariableImporter, ArgvVariableImporter
from variable_manager.handlers import PromptInputHandler, AlwaysPromptInputHandler

class TestVariable(unittest.TestCase):
    def test_variable_initialization(self):
        var = Variable(name="test", value="123", description="Test variable", value_type="integer")
        self.assertEqual(var.name, "test")
        self.assertEqual(var.get_value(), 123)
        self.assertEqual(var.description, "Test variable")
        self.assertEqual(var.value_type, "integer")

    def test_value_conversion(self):
        var = Variable(name="bool_var", value="true", value_type="logical")
        self.assertTrue(var.get_value())

class TestVariableManager(unittest.TestCase):
    def test_add_and_get_variable(self):
        manager = VariableManager()
        var = Variable(name="username", value="John", description="User's name", value_type="text")
        manager.add_variable(var)
        self.assertEqual(manager.get_value("username"), "John")

    def test_import_from_manager(self):
        manager1 = VariableManager()
        manager2 = VariableManager()

        var1 = Variable(name="age", value=30, value_type="integer")
        manager1.add_variable(var1)
        manager2.import_from_manager(manager1)

        self.assertEqual(manager2.get_value("age"), 30)

class TestImporters(unittest.TestCase):
    def test_env_importer(self):
        manager = VariableManager()
        importer = EnvVariableImporter()
        importer.import_variables(manager)
        self.assertIn("PATH", manager.variables)

    def test_json_importer(self):
        manager = VariableManager()
        importer = JsonVariableImporter("tests/test_data/variables.json")
        importer.import_variables(manager)
        self.assertEqual(manager.get_value("user_name"), "John")

    def test_csv_importer(self):
        manager = VariableManager()
        importer = CsvVariableImporter("tests/test_data/variables.csv")
        importer.import_variables(manager)
        self.assertEqual(manager.get_value("username"), "Jhon")

    def test_argv_importer(self):
        manager = VariableManager()
        sys.argv = ["script.py", "name=Test", "age=25"]
        importer = ArgvVariableImporter()
        importer.import_variables(manager)
        self.assertEqual(manager.get_value("name"), "Test")

class TestHandlers(unittest.TestCase):
    def test_prompt_input_handler(self):
        manager = VariableManager()
        var = Variable(name="username", value=None, description="User's name", value_type="text")
        manager.add_variable(var)

        with unittest.mock.patch('builtins.input', return_value="John"):
            handler = PromptInputHandler()
            handler.import_variables(manager)

        self.assertEqual(manager.get_value("username"), "John")

    def test_always_prompt_input_handler(self):
        manager = VariableManager()
        var = Variable(name="username", value="OldValue", description="User's name", value_type="text")
        manager.add_variable(var)

        with unittest.mock.patch('builtins.input', return_value="NewValue"):
            handler = AlwaysPromptInputHandler()
            handler.import_variables(manager)

        self.assertEqual(manager.get_value("username"), "NewValue")

if __name__ == "__main__":
    unittest.main()
