# 1714 - Comerciante
  # https://www.beecrowd.com.br/judge/pt/custom-problems/view/1714

valorCompra = float(input(""))

lucro1 = (valorCompra * 0.45) + valorCompra
lucro2 = (valorCompra * 0.30) + valorCompra


if valorCompra < 20.00:
  print("Valor de venda: R$%.2f" %(lucro1))
else:
  print("Valor de venda: R$%.2f" %(lucro2))