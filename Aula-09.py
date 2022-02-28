
# Aula 09  -- Criando uma calculadora com Python

def soma(x , y):
    return x + y

def sub(x , y):
    return x - y

def mul(x, y):
    return  x * y

def div(x, y):
    return x / y


print(" Selecione a Operação Desejada: ")
print("1.Somar")
print("2.Subtração")
print("3.Multiplicação")
print("4.Divisão")


while True:
    choice = input("Selecione a opração(1/2/3/4):  ")
    
    if choice in('1', '2', '3', '4'):
        num1 = float(input("Informe o primeito valor:  "))
        num2 = float(input("Informe o segundo valor: "))
        
        if choice == '1':
            print(num1, " + ", num2, " = ", soma(num1, num2))
    
        elif choice == '2':
            print(num1, " - ", num2, " = ", sub(num1, num2))
            
        elif choice == '3':
            print(num1, " * ", num2, " = ", mul(num1, num2))
            
        elif choice == '4':
            print(num1, " / ", num2, " = ", div(num1, num2))
        
        next_calculadora = input("Deseja fazer outro Calculo? (yes, no): ")
        if next_calculadora == "no":
            break
    

    else:
        print("Opção invalida")









