nome_aluno = input("Informe o nome do aluno: ")
tipo_escola = input("Informe o tipo de escola do aluno: \n1. Pública \n2. Particular \n")
nota_bi1 = float(input("Insira a nota do primeiro bimestre: "))
nota_bi2 = float(input("Insira a nota do segundo bimestre: "))
nota_bi3 = float(input("Insira a nota do terceiro bimestre: "))
nota_bi4 = float(input("Insira a nota do quarto bimestre: "))
freq_aluno = int(input("Informe a frequência do aluno: "))

freq_corte =  70
media_corte = 7

media = int((nota_bi1 + nota_bi2 + nota_bi3 + nota_bi4)/4)


if tipo_escola == "2" :
    escola = "particular"
    if media >= media_corte and freq_aluno >= freq_corte:
        resultado = "aprovado"
    else:
        resultado = "reprovado"
elif tipo_escola == '1':
    escola = "publica"
    if media >= media_corte or freq_aluno >= freq_corte:
        resultado = "aprovado"
    else:
        resultado = "reprovado"

print(f'Tipo: {escola} \nFrequência de Corte: {freq_corte}% \nMédia de Corte: {media_corte}')
print(f"{nome_aluno.title()} teve média final de {(media):.2f} e frequência de {(freq_aluno):.2f}%")

'''
#Extra 
if resultado == "reprovado":
    print(f'{nome_aluno.title()}, aluno da escola {escola} está de recuperação')
    nota_rec = float(input("Insira a nota da recuperação: "))
    media_prec = (media + nota_rec)/2

    if media_prec >= media_corte:
        print(f"{nome_aluno.title()} teve média pós recuperação de {(media_prec):.2f}")
        resultado = "aprovado pós recuperação"
    else:
        print(f"{nome_aluno.title()} teve média pós recuperação de {(media_prec):.2f}")

'''
print(f'{nome_aluno.title()}, aluno da escola {escola} está {resultado} pela direção')
