# 1760 - Pesquisa - Idade e Peso
    # https://www.beecrowd.com.br/judge/pt/custom-problems/view/1760

mais90 = 0
idades = 0
for c in range(4):
    idade = int(input())
    idades += idade
    peso = float(input())
    if peso > 90:
        mais90 += 1

media = idades / 4
print(f"Qtd pessoas > 90 Kg: {mais90}")
print(f"Idade média: {media:.2f}")