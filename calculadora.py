executar = True
def decisao():
    global executar
    repetir = input("Deseja realizar outra conta? ").lower()
    if repetir == '1' or repetir == 'não':
        executar = False
while executar:
    escolhas = '''
    [1] ou [+] para somar
    [2] ou [-] para subtrair
    [3] ou [*] para multiplicar
    [4] ou [/] para dividir
    [5] ou [//] para divisão inteira
    [6] ou [%] para módulo
    [7] ou [^] para potência
    [8] ou [S] para sair
    (ou digite sua opção para somar/subtrair/multiplicar/dividir/dividir inteiro/modulo/potencia/sair)
    '''
    print(escolhas)
    operador = input('Qual a sua opção? ').lower()
    if operador == '8' or operador == 's':
        executar = False
    else:
        valor01 = float(input("Escolha seu primeiro valor"))
        valor02 = float(input("Escolha seu segundo valor "))
    textinho = '''
    [1] Não, desejo sair!
    [2] Sim, desejo realizar outro cálculo.
    (ou digite sim / não)
    '''
    # ------- Operação de Soma ------- 
    if operador == '1' or operador == "+" == "somar":
        resultado = valor01 + valor02
        print(f'O resultado é {resultado:.2f}')
        print(textinho)
        decisao()
    # ------- Operação de Subtração ------- 
    elif operador == '2' or operador == "-" == "subtrair":
        resultado = valor01 - valor02
        print(f'O resultado é {resultado:.2f}')
        print(textinho)
        decisao()
    # ------- Operação de Multiplicação ------- 
    elif operador == '3' or operador == "*" == "multiplicar":
        resultado = valor01 * valor02
        print(f'O resultado é {resultado:.2f}')
        print(textinho)
        decisao()
    # ------- Operação de Divisão ------- 
    elif operador == '4' or operador == "/" == "dividir":
        if valor02 == 0:
            print("Erro, impossivel dividir por 0")
            print(textinho)
            decisao()
        else:
            resultado = valor01 / valor02
            print(f'O resultado é {resultado:.2f}')
            print(textinho)
            decisao()
    # ------- Operação de Divisão Inteira ------- 
    elif operador == '5' or operador == "//" == "dividir inteiro":
        if valor02 == 0:
            print("Erro, impossivel dividir por 0")
            print(textinho)
            decisao()
        else:
            resultado = valor01 // valor02
            print(f'O resultado é {resultado:.2f}')
            print(textinho)
            decisao()
    # ------- Operação de Módulo ------- 
    elif operador == '6' or operador == "%" == "modulo":
        resultado = valor01 % valor02
        print(f'O resultado é {resultado:.2f}')
        print(textinho)
        decisao()
    # ------- Operação de Potencia ------- 
    elif operador == '7' or operador == "**" == "potencia":
        resultado = valor01 ** valor02
        print(f'O resultado é {resultado:.2f}')
        print(textinho)
        decisao()  
while not executar:
    print("...Saindo da calculadora. Obrigado por usar!")
    print('------ Fim do Sistema ------')
    break

