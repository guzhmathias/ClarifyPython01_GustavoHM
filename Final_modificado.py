import pandas as pd
import numpy as np

# Classe que representa a tabela do imposto de renda (IR)
class TabelaIr:
    def __init__(self):
        # Lista de dicionarios com as faixas salariais e valores
        self.tabela = [
            {"Faixa":(0, 2259.20), "Aliquota": 0, "Dedução": 0}, 
            {"Faixa":(2259.21, 2826.65), "Aliquota": 7.5, "Dedução": 169.44},
            {"Faixa":(2826.66, 3751.05), "Aliquota": 15, "Dedução": 381.44},
            {"Faixa":(3751.06, 4664.68), "Aliquota": 22.5, "Dedução": 662.77},
            {"Faixa":(4664.69, float("inf")), "Aliquota": 27.5, "Dedução": 896.00}
        ]
        
    def calcular_imposto(self, salario_bruto):
        imposto = 0
        for faixa in self.tabela:
            if faixa["Faixa"][0] < salario_bruto <= faixa["Faixa"][1]:
                imposto = (salario_bruto * faixa["Aliquota"]) / 100 - faixa["Dedução"]
                break
        return imposto

# Criar dados com o numpy
nomes = ['Caio', 'Myke', 'Gustavo', 'João', 'Gabriel', 'Luiz']
idades = np.random.randint(20, 50, size=len(nomes))
salarios = np.random.randint(3000, 10000, size=len(nomes))

# Criar o dataframe com o pandas
df = pd.DataFrame({
    "Nome": nomes,
    "Idade": idades,
    "Salários": salarios
})

print(f"\n 📊 Dados iniciais do DataFrame:\n{df}")

# Criar instância da tabela de impostos
tabelaIR = TabelaIr()

# Calcular o imposto para cada pessoa no dataframe
df['Imposto'] = df['Salários'].apply(tabelaIR.calcular_imposto) #Função apply aplica uma função de classe a tabela 

print(f"\nDataframe com nova coluna de impostos calculados: \n{df}")

# Usando as funções do numpy no DataFrame
print(f"Idade média do grupo: \n{np.mean(df['Idade']):.2f}")
print(f"Salário médio do grupo: \n{np.mean(df['Salários']):.2f}")

# Filtrar com pandas pessoas com salário acima da média
media_salario = df['Salários'].mean()
print(f'\nPessoas com salário acima da média: \n{df[df['Salários'] > media_salario]}')

# Estatísticas resumidas
print(f"\nResumo estatístico (pandas): \n{df.describe()}")