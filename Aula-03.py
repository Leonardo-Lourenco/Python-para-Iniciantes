"""


 1 - Estrutura de tomadas de decisão: IF , ELIF, ELSE
 
 2 - Laço FOR
 
 3 - Laço WHILE
 
 4 - BREAK and CONTINUE


"""


# Exemplo: Vamos fazer um programa para verificar se o valor é positivo - IF , ELIF,  ELSE:


"""


num = -10

if num > 0:
    print(num, "valor positivo")
elif num == 0:
    print("Valor Zero")
else:
    print("valor negativo")
    
    



num = float(input("Informe um Valor: "))

if num >= 0:
    if num == 0:
        print("Zero")
        
    else:
        print("Valor Positivo")
else:
    print("Valor negativo")
    




    
"""


"""


#  2 - Laço FOR


# Programa para somar todos os valores de uma LISTA

numeros = [6, 5, 3, 8, 4, 2, 5, 4, 11]

soma = 0


for val in numeros:
    soma = soma+val
    
print("A soma dos valores é:", soma)    




"""






#  3 - Laço WHILE

# soma de todos os valoes = 1+2+3 ...n

n = int(input("Informe um valor: ")) 

soma = 0
i = 1

while i <= n:
    soma = soma + i
    i = i+1
    
print("A soma é: ", soma)    
    

"""

# WHILE COM ELSE

cotador = 1

while cotador < 3:
    print("dentro do laço WHILE")
    cotador = cotador + 1
else:
    print("Condição ELSE")



"""

"""

#BREAK and CONTINUE



for val in "string":
    if val == "i":
        break
    print(val)
    
print("FIM")    
    


#exemplo 02 com s instrução CONTINUE


for val in "string":
    if val == "i":
        continue
    print(val)
    
print("FIM") 


"""

