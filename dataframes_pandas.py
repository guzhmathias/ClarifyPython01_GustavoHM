import pandas as pd

# Criar um dataframe com o  pandas e inserir dados

data = {
    "Nome": ['Caio','Myke','Gustavo','João','Gabriel','Luiz'],
    "Idade": [38,35,22,37,39,44],
    "Salário": [7192,7843,3829,4847,5647,6834]
}

df = pd.DataFrame(data)

# Exibindo o Dataframe
print(f"Dataframe: \n{df}")
print(f"Nomes: \n{df['Nome']}")

# Filtrando linhas (ex: idade menor que 30)
print(f"Pessoas com idade menor que 30 anos: \n{df[df['Idade']<30]}")

# Adicionando uma nova coluna
df['Imposto'] = df['Salário']* 0.18
print(f"Dataframe com nova coluna de impostos calculado: \n{df}")

# Calculando a média de salário
media_salario = df['Salário'].mean()
print(f"Média Salarial: \n{media_salario}")

# Salvar o dataframe em um arquivo CSV

df.to_csv("equipe.csv", index=False)