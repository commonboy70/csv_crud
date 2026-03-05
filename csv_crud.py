import csv

ARQUIVO = "dados.csv"


# Cria um novo registro no CSV
def criar_registro(id, nome, idade):
    with open(ARQUIVO, mode="a", newline="", encoding="utf-8") as arquivo:
        writer = csv.writer(arquivo)
        writer.writerow([str(id), nome, str(idade)])

# Retorna todos os registros do CSV
def listar_registros():
    with open(ARQUIVO, newline="", encoding="utf-8") as arquivo:
        reader = csv.reader(arquivo)
        for linha in reader:
            print(linha)

# Altera um registro do CSV com base no seu id
def atualizar_registro(id_alvo, novo_nome, nova_idade):
    id_alvo = str(id_alvo)
    linhas = []

    with open(ARQUIVO, newline="", encoding="utf-8") as arquivo:
        reader = csv.reader(arquivo)
        cabecalho = next(reader)
        linhas.append(cabecalho)

        for linha in reader:
            if linha and linha[0] == id_alvo:
                linhas.append([id_alvo, novo_nome, str(nova_idade)])
            else:
                linhas.append(linha)

    with open(ARQUIVO, mode="w", newline="", encoding="utf-8") as arquivo:
        writer = csv.writer(arquivo)
        writer.writerows(linhas)

# Remove um registro do CSV com base no seu id
def deletar_registro(id_alvo):
    id_alvo = str(id_alvo)
    linhas = []

    with open(ARQUIVO, newline="", encoding="utf-8") as arquivo:
        reader = csv.reader(arquivo)
        cabecalho = next(reader)
        linhas.append(cabecalho)

        for linha in reader:
            if linha[0] != id_alvo:
                linhas.append(linha)

    with open(ARQUIVO, mode="w", newline="", encoding="utf-8") as arquivo:
        writer = csv.writer(arquivo)
        writer.writerows(linhas)


# Testes manuais (descomente para usar)
# criar_registro(1, "Marcelo Rodrigues", 21)
# listar_registros()
# atualizar_registro(1, "Marcia Pinheiros", 32)
# deletar_registro(1)