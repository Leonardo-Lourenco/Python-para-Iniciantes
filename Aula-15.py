
# Aula 15  -- Dicionários  em Python

# myDict = {1: 'maca', 2: 'bola'}

#myDict = {'nome': 'Leo', 1: [2,4,3]}

#print(myDict)

#print(myDict)


# Acessa os elementos de um dicionário


# dicionario = {'name': 'Leo', 'idade': 28}

# print(dicionario['name'])

#print(dicionario.get('endereco'))




# Acessa alrerando os dados de um dicionário


"""

dicionario = {'nome': 'Leo', 'idade': 28}

print(dicionario)


dicionario['idade'] = 26

print(dicionario)

dicionario['nome']  = 'Leonardo'

print(dicionario)


dicionario['endereco']  = 'VB'

print(dicionario)


"""



# Removendo os itens do dicionario

valores = {1: 1, 2:4, 3: 9, 4: 16, 5: 25}

print(valores.pop(4))

print(valores)


print(valores.popitem())

print(valores)


valores.clear()

print(valores)

del valores

print(valores)


