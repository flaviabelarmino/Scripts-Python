# Desafio 29 - Radar eletrônico
# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$ 7,00 por cada Km acima do limite.

carro = float(input("Insira a velocidade do carro: "))
multa = carro-80
if carro > 80:
    print(f"Você excedeu o limite de velocidade (80Km/h).\nVocê foi multado em R$ {multa*7:.2f}.")
else:
    print("Você está dentro da velocidade limite de (80km/h).")