# 1713 - Salário 02
  # https://www.beecrowd.com.br/judge/pt/custom-problems/view/1713

valorHora = float(input(""))
horaTrabalhada = float(input(""))

salarioBruto = (valorHora * horaTrabalhada)
INSS = (salarioBruto * 0.08)
sindicato = (salarioBruto * 0.05)
impostoRenda = (salarioBruto * 0.11)
salarioliquido = (salarioBruto - INSS - sindicato - impostoRenda)

print("Salário bruto: R$%.2f\nImposto: R$%.2f\nINSS: R$%.2f\nSindicato: R$%.2f\nLíquido: R$%.2f" %(salarioBruto,impostoRenda, INSS, sindicato, salarioliquido))