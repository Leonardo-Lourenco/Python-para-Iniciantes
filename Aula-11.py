

# Aula 11  -- Python List  // Listas em Python


# Adicionar  /   alterar elementos da lista

"""



listExample = [2, 4, 6, 8]
print(listExample)

listExample[0]  = 1
print(listExample)

listExample[0:2] = [3 , 5, 7]
print(listExample)

listExample.append(10)
print(listExample)

listExample.extend([11, 12, 13])
print(listExample)


print(listExample + [14,15,16])

print(["Co"]  * 3)


listExample = [1, 9]
listExample.insert(1,3)
print(listExample)






# Excluir elementos da lista


myList = ['c', 'o', 'o', 'f', 'f', 'e', 'e']



del myList[2]

print(myList)

del myList[1:5]
print(myList)

del myList
print(myList)







myList = ['c', 'o', 'o', 'f', 'f', 'e', 'e']

#myList.remove('c')
print(myList)


print(myList.pop(1))

myList.clear()

print(myList)


"""

# Testando de um determinado elemento está na Lista


myList = ['c', 'o', 'o', 'f', 'f', 'e', 'e']

print('e' in myList)


for frutas in ['maca', 'banana', 'morango']:
    print("Eu gosto  de: ", frutas)








