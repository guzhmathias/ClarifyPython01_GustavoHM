#classe base (superclasse) que representa o animal
class Animal:
    def fazerSom(self):
        # metodo generico que será sobreescrito pelas subclasses
        # o uso do pass indiica que não há implementação aqui
        pass
#classe que herda de animal e representa cachorro
class Cachorro(Animal):
    def fazerSom(self):
        #implementação especifica para cachorros
        return "Au Au!"
    
class Gato(Animal):
    def fazerSom(self):
        return "Miau!"

class Porco(Animal):
    def fazerSom(self):
        return "Oink!" 

#Função que recebe qualquer objeto do tipo animal (ou subclasse)
#E chama o metodo fazerSom() - uso efetivo do polimorfismo
def fazerAnimalfalar(animal: Animal):
    print(animal.fazerSom())

#Criando os objetos
cachorro = Cachorro()
gato = Gato()
porco = Porco()

#Chaman o metodo de cada animal de forma polimorfica

fazerAnimalfalar(cachorro)
fazerAnimalfalar(gato)
fazerAnimalfalar(porco)

#Usando lista de animais (laço + polimorfismo)

animais = [Cachorro(), Gato(), Porco()]

for animal in animais:
    fazerAnimalfalar(animal)