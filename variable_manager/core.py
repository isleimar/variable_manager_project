from typing import Any, Optional, Dict

class Variable:
    def __init__(self, name: str, value: Optional[Any] = None, description: str = "", value_type: str = "text"):
        self.name = name
        self.description = description
        self.value_type = value_type
        self.value = self._convert_value(value)

    def _convert_value(self, value: Any):
        if value is None:
            return None
        if self.value_type == "integer":
            return int(value)
        elif self.value_type == "real":
            return float(value)
        elif self.value_type == "text":
            return str(value)
        elif self.value_type == "logical":
            return value.lower() in ["true", "1", "yes"] if isinstance(value, str) else bool(value)
        elif self.value_type == "date":
            from datetime import datetime
            return datetime.fromisoformat(value)
        else:
            raise ValueError(f"Unsupported value type: {self.value_type}")

    def set_value(self, value: Any):
        self.value = self._convert_value(value)

    def get_value(self):
        return self.value

    def is_empty(self):
        return self.value is None

    def __repr__(self):
        return f"Variable(name={self.name}, value={self.value}, type={self.value_type}, description={self.description})"

class VariableManager:
    def __init__(self):
        self.variables: Dict[str, Variable] = {}

    def add_variable(self, variable: Variable, overwrite_if_none: bool = False):
        if variable.name in self.variables:
            existing = self.variables[variable.name]
            if overwrite_if_none or variable.value is not None:
                existing.set_value(variable.value)
                existing.description = variable.description or existing.description
                existing.value_type = variable.value_type or existing.value_type
        else:
            self.variables[variable.name] = variable

    def get_variable(self, name: str):
        if name not in self.variables:
            raise ValueError(f"Variable '{name}' not found.")
        return self.variables[name]

    def get_value(self, name: str):
        return self.get_variable(name).get_value()

    def import_from_manager(self, other_manager: 'VariableManager', overwrite_if_none: bool = False):
        for variable in other_manager.variables.values():
            self.add_variable(variable, overwrite_if_none=overwrite_if_none)

    def __repr__(self):
        return f"VariableManager(variables={list(self.variables.values())})"