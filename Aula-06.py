
# Aula 06 : Funções Recursiva em Python

def fatorial(x):
    
    if x == 1:
        return 1
    else:
        return(x * fatorial(x - 1)) # 3 * fatorial (2) # 3 * 2 * fatorial (1) # 3 * 2 * 1 e retorna valendo 1
    
num = 3
print("O fatorial de: ", num , "é: ", fatorial(num))