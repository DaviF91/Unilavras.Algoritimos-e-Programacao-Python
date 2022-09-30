# Escreva uma função em Python que calcule o comprimento da hipotenusa de um triângulo retângulo, ao serem fornecidos os catetos. A função deve receber dois parâmetros do tipo float e retornar a hipotenusa com o tipo float.

import math

lado1 = float(input('Informe o 1° lado:'))
lado2 = float(input('Informe o 2° lado:'))

def calcularHipotenusa(lado1, lado2):
    resultadoHip = math.sqrt((lado1 ** 2 + lado2 ** 2))
    return resultadoHip

valorHipotenusa = calcularHipotenusa(lado1, lado2)
print(("A hipotenusa do triângulo com lados: %.2f"%(lado1) + " e %.2f"%(lado2) + " é: %.2f"%(valorHipotenusa)))