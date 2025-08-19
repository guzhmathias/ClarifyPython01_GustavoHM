import requests , json

pedido = input('Qual nome você gostaria de pesquisar?').lower()
resposta = requests.get(f"https://servicodados.ibge.gov.br/api/v2/censos/nomes/{pedido}")

dados = json.loads(resposta.text)

print(dados[0]["res"][8])