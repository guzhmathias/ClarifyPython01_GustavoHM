def minhaFuncao() :
    print("Olá Clarify!")

minhaFuncao()

cidades = ['São Paulo', 'Osasco', 'POA', 'São Bernardo do Campo']
cidades2 = ['Suzano', 'Mogi das Cruzes', 'Diadema', 'Mauá']
contador = 0

def minhaFuncaoMelhorada(local , giro):
    print(str(giro) + '-' + local)

for cidade in cidades:
    contador += 1
    minhaFuncaoMelhorada(cidade, contador)
contador = 0
for cidade in cidades2:
    contador += 1
    minhaFuncaoMelhorada(cidade, contador)