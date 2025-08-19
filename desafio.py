from random import randint

#Jogo de adivinhação com diversos gatilhos

validador = True

def fimdejogo():
    print("############# Fim do Jogo #############")
    print("--------- Obrigado por Jogar ---------\n")


def jogo(chancesEas):
    global validador
    while validador:
        for chutes in range (chancesEas):
            tentativa = (input(f"Chute um número de {menor} a {maior}\n"))
            if tentativa.isnumeric():
                tentativa = int(tentativa)
            if tentativa > random:
                chancesEas -= 1
                print(f"O número para adivinhar é menor \nVocê tem {chancesEas} chances")
            elif tentativa < random:
                chancesEas -= 1
                print(f"O número para adivinhar é maior \nVocê tem {chancesEas} chances")
            else:
                print(f'Parabéns você acertou o número {random} com {chancesEas} chances restantes')
                fimdejogo()
                validador = False
                break
            if chancesEas == 0:
                print(f"Poxa que pena, você perdeu! o número para adivinhar era {random}")
                fimdejogo()
                validador = False
                break

 
print("############# Início do Jogo #############")
print("----------- Adivinhe o Tesouro -----------\n")
print("-------- Feito por: Gustavo Mathias --------\n")

dif = input('''
            Selecione a dificuldade
            [1] Fácil
            [2] Médio
            [3] Difícil
            ''')
if dif == '2':
    maior = 300
elif dif =='3':
    maior = 1000
else:
    maior = 100

menor = 0
chancesEas = int(0.1* maior)
random = randint(0, maior)
jogo(chancesEas)