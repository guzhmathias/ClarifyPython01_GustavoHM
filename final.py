
import pandas as pd
import numpy as np

'''  
# Classe que representa a tabela do imposto de renda (IR)
class TabelaIr:
    def __init__(self):
        # Lista de dicionarios com as faixas salariais e valores
        self.tabela = [
            {"Faixa":(0,2259.20),"Aliquota":0, "Dedução":0}, 
            {"Faixa":(2259.21,2826.65),"Aliquota":7.5, "Dedução":169.44},
            {"Faixa":(2826.66,3751.05),"Aliquota":15, "Dedução":381.44},
            {"Faixa":(3751.06,4664.68),"Aliquota":22.5, "Dedução":662.77},
            {"Faixa":(4664.69,float("inf")),"Aliquota":27.5, "Dedução":896.00}
        ]

## Classe responsavel pelo calculo do IR com base na tabela
class CalculadoraIR:
    def __init__ (self, salarioBruto, tabelaIR):
        self.salarioBruto = salarioBruto
        self.tabelaIR = tabelaIR
    
    def calcular(self):
        imposto = 0 # Inicializa com imposto zerado
        for faixa in self.tabelaIR.tabela:
        # Percorre cada faixa da tabela
            if self.salarioBruto > faixa["Faixa"][0] and self.salarioBruto <= faixa["Faixa"][1]:
                imposto = (self.salarioBruto*faixa["Aliquota"])/100 - faixa["Dedução"]
                break
        return imposto
 ''' 

# Criar dados com o numpy

nomes = ['Caio','Myke','Gustavo','João','Gabriel','Luiz']
idades = np.random.randint(20,50, size=len(nomes))
salarios = np.random.randint(3000,10000, size=len(nomes))

# Criar o dataframe com o pandas
df = pd.DataFrame({
    "Nome": nomes,
    "Idade": idades,
    "Salários": salarios
})

print(f"\n 📊\n{df}")

# Adicionar nova coluna de imposto
'''
tabelaIR = TabelaIr()
calculadora = CalculadoraIR(df['Salários'], tabelaIR)
'''

df['Imposto'] = df['Salários']* 0.18
print(f"Dataframe com nova coluna de impostos calculado: \n{df}")

# Usando as funcoes do numpy no DataFrame
print(f"Idade média do grupo \n{np.mean(df['Idade']):.2f}")
print(f"Salário médio do grupo \n{np.mean(df['Salários']):.2f}")

# Filtrar com pandas pessoas com salário acima da média
media_salario = df['Salários'].mean()
print(f'\n Pessoas com salário acima da média \n{df[df['Salários'] > media_salario]}')

# Estatisticas resumidas
print(f"\n Resumo estatístico (pandas) {df.describe()}")