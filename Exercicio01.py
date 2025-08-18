#Exercício:

#Recebe as notas e o nome do aluno
nome_aluno = str(input("Insira o nome do aluno: "))
nota_bi1 = float(input("Insira a nota do primeiro bimestre: "))
nota_bi2 = float(input("Insira a nota do segundo bimestre: "))
nota_bi3 = float(input("Insira a nota do terceiro bimestre: "))
nota_bi4 = float(input("Insira a nota do quarto bimestre: "))

media = (nota_bi1 + nota_bi2 + nota_bi3 + nota_bi4)/4

print(f"{nome_aluno.title()} teve média final de {(media):.2f}")


    