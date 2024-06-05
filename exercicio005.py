#Dada a lista ["maçã", "banana", "cereja"] e o dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}, calcule o preço total da lista de compras.

dicionario: dict = {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}

print(sum(dicionario.values()))