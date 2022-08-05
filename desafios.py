

"""


# 1 : Programa para CALCULAR a Área e Perímetro de um Quadrado, Círculo e Retângulo.

# defining functions

# Calcular o perímetro do Círculo
def perimetro_circulo(raio):
    para = 2 * 3.14 * raio
    print("perímetro do Círculo é: ", para)
    

# Calcular o perímetro do Retângulo
def perimetro_retangulo(height, width):
    para = 2 * ( height + width)
    print("o perímetro do Retângulo é: ", para)
    
# Calcular o perímetro do Quadrado
def perimetro_quadrado(side):
    para = 4 * side
    print("o perímetro do quadrado é: ", para)
    
# Calcular a Área do Círculo
def area_circulo(raio):
    area = 3.14 * raio * raio
    print("Área do Círculo: ", area)
    
# Calcular a Área do Retângulo
def area_retangulo(height, width):
    area = height * width
    print("Área do Retângulo: ", area)

# Calcular a Área do Quadrado
def area_quadrado(side):
    area = side * side
    print("Área do Quadrado: : ", area)


print("")

print("BEM VINDO MENU DE OPÇÕES COM PYHON")

#creating options
while True:
    print("\n MENU")
    print("1. Calcular o Perímetro")
    print("2. Calcular a Área")
    print("3. Sair")
    choice1 = int(input("Selecionar o Opção desejada: "))
    
    if choice1 == 1:
        print("CALCULAR O PERÍMETRO")
        print("1. Circulo")
        print("2. Retângulo")
        print("3. Quadrado")
        print("4. Sair")
        choice2 = int(input("Selecione a opção desejada: "))
        
        if choice2 == 1:
            raio = int(input("Informe o Raio do Círculo:"))
            perimetro_circulo(raio)
            
        elif choice2 == 2:
            height = int(input("Informe a ALTURA do Ratângulo"))
            width = int(input("Informe a LARGURA do Ratângulo"))
            primetro_retangulo(height, width)
            
        elif choice2 == 3:
            side  = int(input("Informe o TAMANHO de um dos lados do Quadrado: "))
            perimetro_quadrado(side)
            
        elif choice2 == 4:
             break
            
        else:
              print("Opsss, opção invalida!!")
              
              
    elif choice1 == 2:
        print("CALCULAR O ÁREA")
        print("1. Circulo")
        print("2. Retângulo")
        print("3. Quadrado")
        print("4. Sair")
        choice3 = int(input("Selecione a opção desejada: "))
        
        if choice3 == 1:
            raio = int(input("Informe o Raio do Círculo:"))
            area_circulo(raio)
            
        elif choice3 == 2:
            height = int(input("Informe a ALTURA do Ratângulo"))
            width = int(input("Informe a LARGURA do Ratângulo"))
            area_retangulo(height, width)
            
        elif choice3 == 3:
            side  = int(input("Informe o TAMANHO de um dos lados do Quadrado: "))
            area_quadrado(side)
            
        elif choice3 == 4:
             break
            
        else:
              print("Opsss, opção invalida!!")
        
    elif choice1 == 3:
        break
        
    else:
        print("Opsss, opção invalida!!!")
        
        



"""








# 2 : Criando uma Calculadora com Python

#Função para SOMAR
def add(a ,b):
    somar = a + b
    print("A soma de ", a, " + ", b, " é ", somar)
    
#Função para SUBTRAÇÃO
def subtract(a, b):
    subtracao = a - b
    print(a, " - ", b, " = ", subtracao)
    
#Função  MULTIPLICAÇÃO
def multiply(a ,b):
    multiplicacao = a * b
    print(a ," * ", b, " = ", multiplicacao)

#Função  DIVISÃO
def  divide(a, b):
    divisao = a / b
    print(a ," / ", b, " = ", divisao)
    

print("")
print("BEM VINDO CALCULADORA CURSO DE PYTHON")


while True:
    print("\nMENU")
    print("1. SOMAR")
    print("2. SUBTRAÇÃO")
    print("3. MULTIPLIAÇÃO")
    print("4. DIVISÃO")
    print("5. Sair")
    choice = int(input("\n Selecione a opção desejada: "))
    
    if choice == 1:
        print("\nSOMAR")
        a = int(input("INformar um valor: "))
        b = int(input("INformar um segundo valor: "))
        add(a, b)
        
    elif choice == 2:
        print("\nSUBTRAÇÃO")
        a = int(input("Informar um valor: "))
        b = int(input("Informar um segundo valor: "))
        subtract(a, b)
        
    elif choice == 3:
        print("\nMULTIPLICAÇÃO")
        a = int(input("Informar um valor: "))
        b = int(input("Informar um segundo valor: "))
        multiply(a, b)
        
    elif choice == 4:
        print("\nDIVISÃO")
        a = int(input("Informar um valor: "))
        b = int(input("Informar um segundo valor: "))
        divide(a, b)
        
    elif choice == 5:
        break
    
    else: print("Opção invalida")
        
        
    
    

    



















