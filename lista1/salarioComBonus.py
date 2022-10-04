# 1009 - Salário com Bônus
  # https://www.beecrowd.com.br/judge/pt/problems/view/1009

nome = input("")
salarioFixo = float(input(""))
totalVendas = float(input(""))


TOTAL = (salarioFixo + (totalVendas * 0.15))

print("TOTAL = R$ %0.2f" %(TOTAL))