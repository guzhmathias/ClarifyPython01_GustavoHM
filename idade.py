
def funcao():
    executar = True

    while executar:
        try:
            anoNasc = int(input("Em que ano você nasceu? "))
            anoAtual = int(input("Em que ano estamos? "))
            idade = anoAtual - anoNasc
            print(f"Você tem {idade} anos")
        except ValueError:
            print("Por favor, digite um número válido para os anos")

        opcao = str(input("\nDeseja testar novamente? \nSim \nNão\n")).strip().lower()

        '''
        lista = ["não","nao",'n']
        if opcao in lista:
            executar = False
        '''

        if opcao in ["não","nao",'n']:
            executar = False
funcao()