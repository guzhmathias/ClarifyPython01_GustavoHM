import pandas as pd

# Carregar um arquivo do Excel
def carregarCSV(caminhoArquivo):
    # Carrega os dados do arquivo csv em um dataframe
    df = pd.read_csv(caminhoArquivo)
    print("Arquvivo carregado com sucesso!")
    print(df.head())
    return df
# Salvar um arquivo modificado em CSV
def salvarCSV(df, caminhoSaida):
    df.to_csv(caminhoSaida, index=False)
    print(f"Arquivo Salvo com sucesso em {caminhoSaida}")
# Salvar um arquivo modificado em XLSX
def salvarXLSX(df, caminhoSaida):
    df.to_excel(caminhoSaida, index=False)
    print(f"Arquivo Salvo com sucesso em {caminhoSaida}")

def carregarXLS(caminhoArquivo):
    # Carrega os dados do arquivo xlsx em um dataframe
    df = pd.read_excel(caminhoArquivo)
    print("Arquvivo carregado com sucesso!")
    print(df.head())
    return df

# Local onde está o arquivo a ser carregado

localArquivo = "C:/Users/integral/Desktop/ClarifyPython01_GustavoHM-main/base.csv"
# Utilizando o caminho inteiro até o arquivo
# Nota: Inverter as barras quando for copiar o caminho do arquivo
localArquivo2 = "base.csv"
# Caso o arquivo de Database esteja no mesmo lugar do executavel em python
# Chamando apenas pelo nome do arquivo

df = carregarCSV(localArquivo)
df2 = carregarCSV(localArquivo2)

df["Comissao"] = df["Vendas"] * 0.25

'''
df["Media de Vendas"] = (df["TV"] + df["Radio"] + df["Jornal"])/3

'''
#Criar Nova coluna no arquivo (com base na média entre os 3 canais)
df["Media Comercial"] = df[["TV", "Radio", "Jornal"]].mean(axis=1)
print(df.head())

caminhoSaida = "C:/Users/integral/Desktop/ClarifyPython01_GustavoHM-main/novo_arquivo.csv"

# Salvando um novo arquivo e selecionando a pasta/caminho onde o arquivo será salvo

nome = input("Insira o nome do novo arquivo: \n")
caminhoPrincipal = "C:/Users/integral/Desktop/ClarifyPython01_GustavoHM-main/"
#Solicitar o nome do arquivo novo

tipo = input("Deseja exportar para: \n[1]Excel \n[2]CSV \n")
#Solicitar o tipo do arquvio

#Validador para salvar em Excel, CSV, ou em caso de erro exibir mensagem
if tipo == '1':
    salvarXLSX(df, f"{caminhoPrincipal}{nome}.xlsx")
elif tipo == '2':
    salvarCSV(df, f"{caminhoPrincipal}{nome}.csv")
else:
    print("Por favor, selecione uma opção válida")

    