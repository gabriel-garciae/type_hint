#Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação. Imprima cada informação.

#dicionario
dicionario: dict = {
    "livro": "os segredos da mente milionaria",
    "autor": "desconhecido",
    "ano": 2007
}

#retornar chave e valor
print(dicionario.items())

#retornar apenas as chaves
print(dicionario.keys())

#retornar apenas valores
print(dicionario.values())