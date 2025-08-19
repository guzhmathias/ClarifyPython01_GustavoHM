def calcularIR(salarioBruto):
    tabelaIR = [
        {"Faixa":(0,2259.20),"Aliquota":0, "Dedução":0}, 
        {"Faixa":(2259.21,2826.65),"Aliquota":7.5, "Dedução":169.44},
        {"Faixa":(2826.66,3751.05),"Aliquota":15, "Dedução":381.44},
        {"Faixa":(3751.06,4664.68),"Aliquota":22.5, "Dedução":662.77},
        {"Faixa":(4664.69,float("inf")),"Aliquota":27.5, "Dedução":896.00}
        ] 

    imposto = 0
    for faixa in tabelaIR:
        if salarioBruto > faixa["Faixa"][0] and salarioBruto <= faixa["Faixa"][1]:
            imposto = (salarioBruto*faixa["Aliquota"])/100 - faixa["Dedução"]
            break
    return imposto 

salarioBruto = float(input("Informe seu salário bruto: "))

imposto = calcularIR(salarioBruto)
salarioLiq = salarioBruto - imposto
print(f"O imposto de renda devido é de R$ {imposto:.2f} \nSeu salário líquido é de {salarioLiq:.2f}")