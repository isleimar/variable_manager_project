# Arquitetura e Design

## Visão Geral

O projeto foi desenvolvido com modularidade em mente, separando a lógica principal (core) das extensões e manipuladores. Isso facilita a adição de novas fontes de dados ou comportamentos interativos sem alterar o núcleo do sistema.

## Componentes

### 1. Core
- **Variable**: Representa uma variável com nome, valor, tipo e descrição.
- **VariableManager**: Gerencia uma coleção de variáveis e fornece métodos para adicionar, atualizar e consultar variáveis.

### 2. Importers
- Classes como `JsonVariableImporter` e `CsvVariableImporter` implementam a interface `VariableImporter` para importar variáveis de diferentes fontes.

### 3. Handlers
- Manipulam variáveis interativamente, por exemplo, pedindo entrada do usuário para variáveis sem valor (`PromptInputHandler`).

### 4. Extensibilidade
- Novos importadores e manipuladores podem ser adicionados facilmente, seguindo a interface base.

## Fluxo de Dados

1. Variáveis são criadas manualmente ou importadas de uma fonte externa.
2. Se necessário, manipuladores interativos solicitam entrada para variáveis sem valor.
3. O `VariableManager` mantém uma coleção das variáveis, garantindo que valores sejam atualizados ou criados conforme necessário.

## Decisões de Design

- **Separação de responsabilidades**: Core, importers e handlers têm responsabilidades distintas.
- **Flexibilidade para extensões**: Facilmente expansível com novas fontes de dados ou manipuladores.
- **Validação de tipos**: Conversão automática dos valores para o tipo especificado (e.g., texto, inteiro, lógico).
