#with é um gerenciador de contexto, ele abre e fecha um contexto
#api nativa do python, ler um arquivo csv sem usar o pandas ou outra biblioteca
#se exsite um processo que todo mundo faz, é melhor criar uma função em um módulo, comunicar entre o time para todo mundo usar ela. Evita bugs

import csv

caminho_arquivo = 'exemplo.csv'

dados = []

with open(caminho_arquivo, mode='r', encoding='utf-8') as arquivo:
    # Cria um objeto leitor de csv
    leitor_csv = csv.DictReader(arquivo)

    # Itera sobre as linhas do arquivo csv
    for linha in leitor_csv:
        dados.append(linha)

# Exibe os dados lidos do arquivo csv
for registro in dados:
    print(registro)   