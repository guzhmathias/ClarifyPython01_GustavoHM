# Entendendo for e while, conceitos de loopings

palavra = "Tubarão"
contador = 0

for letra in palavra:
    print(str(contador)+'-'+letra)
    contador += 1

cidades = ['São Paulo', 'Osasco', 'POA', 'São Bernardo do Campo']

for cidade in cidades:
    print(cidade)

linha = '-' * 20
print(linha)
print(cidades[3])
print(linha)

linha1 = '-' * 5
print (linha1,'Trabalhando com While', linha1)
botao_executar = True #Boolean true/false
contador = 0

while botao_executar:
    print(contador)
    contador += 1
    if contador >= 10:
        botao_executar = False

print('Fim do Looping')