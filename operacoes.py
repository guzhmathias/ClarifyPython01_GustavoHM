def soma(a,b):
    return a + b
def subtra(a,b):
    return a - b
def multip(a,b):
    return a * b
def dividir(a,b):
    if b == 0:
        raise ValueError('Não foi possível dividir por 0')
    else:
        return a / b
def dividirI(a,b):
    if b == 0:
        raise ValueError('Não foi possível dividir por 0')
    else:
        return a // b
def restoDiv(a,b):
    return a % b
def potenc(a,b):
    return a ** b
def fatorial(c):
    resultado = 1
    for i in range(c, 0, -1):
        resultado *= i
    return resultado
