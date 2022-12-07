# Desafio 10 
# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos
# dólares ela pode comprar. (Considere US$1,00=R$5,32).

real=float(input('Insira o valor em R$ que você possui: '))
dolar=real/5.32
print(f'{dolar:.2f}')
