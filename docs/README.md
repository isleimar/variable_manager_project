# README.md

# Variable Manager Project

**Variable Manager** é um sistema em Python para gerenciar variáveis de diferentes tipos, com suporte a extensões para importar valores de diversas fontes (JSON, CSV, variáveis de ambiente, argumentos de linha de comando, etc.) e manipular variáveis via entrada do usuário.

## Funcionalidades principais

- Gerenciamento de variáveis com tipos definidos (texto, número inteiro, número real, data, lógico).
- Suporte a múltiplas extensões para importar variáveis de fontes externas.
- Entrada interativa para variáveis sem valor definido (NULL).
- Atualização de valores existentes ou criação de novos.
- Modularidade para expandir com novas extensões.

## Instalação

Clone o repositório e instale as dependências:

```bash
git clone <URL_DO_REPOSITORIO>
cd variable_manager_project
pip install -r requirements.txt
```

## Uso básico

Veja exemplos práticos em [examples/example_usage.py](../examples/example_usage.py).

## Testes

Rode os testes usando `pytest`:

```bash
pytest tests/
```