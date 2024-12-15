from .core import VariableManager

class PromptInputHandler:
    def import_variables(self, manager: VariableManager):
        for variable in manager.variables.values():
            if variable.is_empty():
                value = input(f"Enter value for {variable.name} ({variable.description}): ")
                variable.set_value(value)

class AlwaysPromptInputHandler:
    def import_variables(self, manager: VariableManager):
        for variable in manager.variables.values():
            value = input(f"Enter value for {variable.name} ({variable.description}): ")
            variable.set_value(value)