import json, requests

pedido = input("Qual o seu nome? ").lower()

localidade =  0

while localidade < 1 or localidade > 2:
    localidade = int(input("Você deseja selecionar uma localidade? \n1) Sim\n2)Não \n"))

    if localidade == 1:
        uf = input("Qual estado você deseja busca? \n35) SP \n33) RJ \n31) MG \n43) RS \n53 DF\n")
        resultado = requests.get(f"https://servicodados.ibge.gov.br/api/v2/censos/nomes/{pedido}?localidade={uf}")
    if localidade == 2:
        resultado = requests.get(f"https://servicodados.ibge.gov.br/api/v2/censos/nomes/{pedido}")


    print('''
    Escolha o período de tempo
        1) 1930
        2) 1930 - 1940
        3) 1940 - 1950
        4) 1950 - 1960
        5) 1960 - 1970
        6) 1970 - 1980
        7) 1980 - 1990
        8) 1990 - 2000
        9) 2000 - 2010
        ''')
    
    tempo = int(input("Selecione o período ")) - 1
    dados = json.loads(resultado.text)
    print(dados[0]["res"][tempo])
