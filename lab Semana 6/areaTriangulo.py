# Escreva uma função em Python que receba a base e a altura de um triângulo e retorne sua área (A = (base x altura) / 2). A função deve receber dois parâmetros do tipo float e retornar a área com o tipo float.

base = float(input("Informe a base: "))
altura = float(input("Informe a base: "))


def areaTriangulo(base, altura):
    A = base * altura / 2
    return A


valor_soma = areaTriangulo(base, altura)
print("A área do triângulo é:%.2f" % (valor_soma))
