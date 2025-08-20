class Carro:
    def __init__(self,cor,modelo,barulho):
        self.cor = cor
        self.modelo = modelo
        self.barulho = barulho
        self.velocidade = 0
    def acelerar(self, incremento):
        self.velocidade += incremento
        print(f"O carro {self.modelo} acelerou para {self.velocidade} Km/h.")
    def desacelerar(self, incremento, limiteVelocidade):
        while self.velocidade >= limiteVelocidade:
            self.velocidade -= incremento
            print(f"O carro {self.modelo} desacelerou para {self.velocidade} Km/h.")
        if self.velocidade <= limiteVelocidade:
            print(f"O carro {self.modelo} está dentro do limite de velocidade de {limiteVelocidade} Km/h. ")
    def frear(self, incremento):
        while self.velocidade >= incremento:
            self.velocidade -= incremento
            print(f"O carro {self.modelo} desacelerou para {self.velocidade} Km/h.")
        if self.velocidade <= 0:
            self.velocidade == 0
            print(f"O {self.modelo} {self.cor} parou!")
    def parar(self):
        self.velocidade = 0
        print(f"O carro {self.modelo} parou.")
    def buzina(self):
        print(f'O {self.modelo} {self.cor} fez barulho \n{self.barulho}')
# Criando um objeto carro


meu_carro = Carro("Amarelo", "Fusca", "Bibibi")
carro_visita = Carro("Roxo", "Toyota Supra", "VRUUUUM")

meu_carro.acelerar(20)
meu_carro.acelerar(30)
meu_carro.parar()

carro_visita.acelerar(100)
carro_visita.desacelerar(2, 40)
carro_visita.frear(2)
carro_visita.buzina()
carro_visita.parar()

# Criando uma loja de carros

carros = [Carro("Amarelo","Fox","Bippp!!!"),
          Carro("Marrom","Ford Bronco","Bippp!!!"),
          Carro("Vinho","Ford Mustang","Vrumm!!!"),
          Carro("Preto","Lambo Urus","Brumm!!!"),
          Carro("Cinza","MB Classe G","Biip!!!"),
          ]

for carro in carros:
    carro.acelerar(50)
    carro.buzina()

