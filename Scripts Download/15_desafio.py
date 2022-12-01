#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e
#a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar,
#sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por Km rodado.

km=float(input("Insira a quantidade de km percorridos: "))
dias=int(input("Insira a quantidade de dias de aluguel do veículo: "))
carro=60*dias
distancia=0.15*km
print(f"Em {dias} dias você andou {km} km.\nValor total a ser pago R$: {carro+distancia:.2f}")
