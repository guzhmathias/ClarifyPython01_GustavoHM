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

# cria uma instância da tabela de IR
tabelaIR = TabelaIr()
# Solicita o salario bruto do usuario
salarioBruto = float(input("Informe seu salário bruto: "))

calculadora = CalculadoraIR(salarioBruto, tabelaIR)
imposto = calculadora.calcular()
salarioLiq = salarioBruto - imposto
print(f"O imposto de renda devido é de R$ {imposto:.2f} \nSeu salário líquido é de {salarioLiq:.2f}")

