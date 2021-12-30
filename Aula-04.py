
"""


# EXERCICIO 01 : Programa para gerar um valor aleatório de 1 a 9 - OBS: Usar a biblioteca random


# Exercício 02: Programa para verificar se o valor informado é ÍMPAR ou PAR:  OBS: IF e ELSE


# Exercício 03 : Faça um Programa para encontrar o maior número entre três números:  OBS: IF e ELSE


# Exercício 04: Faça um Programa para encontrar o FATORIAL de um NÚMERO:  OBS: IF e ELSE e FOR
# Por exemplo, o fatorial de 6 é 1*2*3*4*5*6 = 720.
# O fatorial não é definido para números negativos e o fatorial de zero é um 0! = 1,.



# Exercćio 05:  Faça um Programa para exibir a Tabela de Multiplicação:  OBS: IF e ELSE e FOR


# Exercćio 06: Programa para IMPRIMIR a SEGUÊNCIA DE FIBONACCI: OBS: IF, ELSE e WHILE

# Uma sequência de Fibonacci é a sequência inteira de 0, 1, 1, 2, 3, 5, 8 .... n..
# Os primeiros dois termos são 0 e 1. Todos os outros termos são obtidos com a soma dos dois temos anteriores.




"""



"""



# EXERCICIO 01 : Programa para gerar um valor aleatório de 1 a 9 - OBS: Usar a biblioteca random

import random

print(random.randint(0,100))









# Exercício 02: Programa para verificar se o valor informado é ÍMPAR ou PAR:  OBS: IF e ELSE

num = int(input("Informe um valor: "))

if(num % 2) == 0:
    print("{0} é PAR".format(num))
else:
    print("{0} é ÍMPAR ".format(num))










# Exercício 03 : Faça um Programa para encontrar o maior número entre três números:  OBS: IF e ELSE


num1 = float(input("Informe o PRIMEIRO valor: "))
num2 = float(input("Informe o SEGUNDO valor: "))
num3 = float(input("Informe o TERCEIRO valor: "))


if(num1 >= num2) and (num1 >= num3):
    maiorNumero = num1
elif(num2 >= num1) and (num2 >= num3):
    maiorNumero = num2
else:
    maiorNumero = num3
    
print(" O maior valor informado é: ", maiorNumero)    

    




# Exercício 04: Faça um Programa para encontrar o FATORIAL de um NÚMERO:  OBS: IF e ELSE e FOR
# Por exemplo, o fatorial de 6 é 1*2*3*4*5*6 = 720.
# O fatorial não é definido para números negativos e o fatorial de zero é um 0! = 1,.


num = int(input("Informe um valor: "))

factorial = 1

if num < 0:
    print("Não existe fatorial para valores NEGATIVOS")
elif num == 0:
    print("Fatorial de 0 é 1")
else:
    for i in range(1,num +1):
        factorial = factorial*i
    print("Fatorial de ", num, "é", factorial)



"""



# Exercćio 05:  Faça um Programa para exibir a Tabela de Multiplicação:  OBS: IF e ELSE e FOR


num = int(input("Informe  o valor que deseja multiplicar:  "))

for i in range(1, 11):
    print(num, 'x', i , '=' , num*i)































