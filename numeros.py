'''

# Tipos de numeros
naonumero = "2" #string (Valor de texto, logo não consegue somar, apenas concatena)
idade = 22 #int (Inteiro/Integer)
altura = 1.89 #Float (Decimal)

print(naonumero + naonumero)
print(idade + 2)
#print("Minha idade é" + idade) -> Valores de texto e valores numéricos não operam entre si
print("Minha idade é " + str(idade))

idade_usuario = int(input('Qual a sua idade?: '))
print("Você tem " + str(idade_usuario) + " anos.")
resultado = idade_usuario + 1
print("Ano que vem você terá " + str(resultado) + " anos")

'''
valor_a = 10
valor_b = 3

print('Soma:', valor_a + valor_b )
print('Subtração:', valor_a - valor_b )
print('Multiplicação:', valor_a * valor_b )
print('Divisão:', valor_a / valor_b ) #Resultado em float
print('Divisão Inteira:', valor_a // valor_b ) #Descarta o decimal
print('Resto da divisão:', valor_a % valor_b ) #Modulo
print('Potência:', valor_a ** valor_b) #a^b

