'''

Aula 01: Tipos de dados e variaveis

-------- strings (Texto) --------

'''
nome = 'Gustavo'
curso = "Python"
mensagem = "Bem vindo " + nome + ' ao curso de ' + curso + '!'

print(mensagem)

#Usando a função f na string
mensagem2 = f"Olá {nome}, seja bem vindo ao curso de {curso}!"

print(mensagem2)

#Algumas funções de string
print(nome.upper()) #Tudo maiusculo
print(nome.lower()) #Tudo minusculo
print(nome.title()) #Primeira letra de cada palavra em maiuscula

#Repetindo strings com o operador de multiplicação

linha = '-' * 20
print(linha)
print('Exercício concluído com sucesso!')
print(linha)

#