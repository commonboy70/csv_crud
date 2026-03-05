# CRUD em CSV com Python

Projeto simples para praticar operações básicas de **CRUD (Create, Read, Update, Delete)** utilizando arquivos CSV e a biblioteca padrão do Python.

## Objetivo

Demonstrar como:
- Ler dados de um arquivo CSV
- Inserir novos registros
- Atualizar registros existentes
- Remover registros
- Reescrever o arquivo de forma segura

Tudo isso **sem usar bibliotecas externas**.

---

## Estrutura do Projeto

csv_crud/
├── csv_crud.py
├── dados.csv
└── README.md

---

## Estrutura do CSV

O arquivo `dados.csv` deve seguir o formato abaixo:

id,nome,idade
1,Ana,20
2,Bruno,25

- Todos os valores são tratados como **string**
- A primeira linha é sempre o **cabeçalho**

---

## Funcionalidades

### Criar registro
Adiciona uma nova linha ao CSV.


criar_registro(1, "Marcelo Rodrigues", 21)

---

### Listar registros

Exibe todas as linhas do CSV no terminal.


listar_registros()

---

### Atualizar registro

Atualiza nome e idade com base no ID.

atualizar_registro(1, "Marcia Pinheiros", 32)

> O registro só é atualizado se o ID existir.

---

### Deletar registro

Remove um registro com base no ID.

deletar_registro(1)

---

## Como executar

1. Certifique-se de ter **Python 3** instalado
2. Coloque o arquivo `dados.csv` na mesma pasta do script
3. Execute:

python csv_crud.py

Os testes podem ser feitos descomentando as chamadas no final do arquivo.

---

## Tecnologias Utilizadas

* Python 3
* Biblioteca padrão `csv`

---

## Observações Importantes

* CSV não possui tipos de dados (tudo é string)
* Atualizações e deleções exigem reescrever o arquivo inteiro
* O cabeçalho é preservado em todas as operações
