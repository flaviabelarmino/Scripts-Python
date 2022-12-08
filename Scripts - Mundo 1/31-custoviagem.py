# Desafio 31 - Custo da viagem
# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$ 0,50 por Km para viagens
# de até 200Km e R$ 0,45 para viagens mais longas.

dist = float(input("Qual a distância da viagem em km? "))
p1 = 0.50*dist
p2 = 0.45*dist

if dist <= 200:
    print(f"O valor da passagem R$: {p1:.2f}")
else:
    print(f"O valor da passagem R$: {p2:.2f}")