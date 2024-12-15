# Documentação de Uso

## Criando variáveis manualmente

```python
from variable_manager.core import Variable, VariableManager

manager = VariableManager()
manager.add_variable(Variable(name="username", value="admin", description="Admin user", value_type="text"))
manager.add_variable(Variable(name="age", value=30, description="User age", value_type="integer"))
```

## Importando variáveis

### Importando de um arquivo JSON

```python
from variable_manager.importers import JsonVariableImporter

json_importer = JsonVariableImporter("variables.json")
json_importer.import_variables(manager)
```

### Importando de um arquivo CSV

```python
from variable_manager.importers import CsvVariableImporter

csv_importer = CsvVariableImporter("variables.csv")
csv_importer.import_variables(manager)
```

### Importando de variáveis de ambiente

```python
from variable_manager.importers import EnvVariableImporter

env_importer = EnvVariableImporter()
env_importer.import_variables(manager)
```

### Entrada manual via prompt

```python
from variable_manager.handlers import PromptInputHandler

prompt_handler = PromptInputHandler()
prompt_handler.import_variables(manager)
```