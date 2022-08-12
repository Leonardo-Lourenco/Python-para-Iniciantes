
# Programação Orientado a Objetos  --  POO  ou OPP

class Papagaio:
    #Atributos: são as carscterísticas de um objeto
    especie = "passaro"
    
    # instanciar os atributos
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
  
    def sing(self, song):
        return "{} sings {}".format(self.nome, song)
    
    def dance(self):
        return "{} agora pode dançar".format(self.nome)

# criando o objeto

blu = Papagaio("Blu", 10)
woo = Papagaio("Woo", 15)

print("")

print("Blu é um {}".format(blu.__class__.especie))
print("Woo tambem é um {}".format(blu.__class__.especie))


print("")

print("{} tem {} de idade".format( blu.nome, blu.idade))
print("{} tem {} de idade".format( woo.nome, woo.idade))


print("")

print(" CHAMANDO SO MÉTODOS")

print(blu.sing("Happy"))
print(blu.dance())


        
        