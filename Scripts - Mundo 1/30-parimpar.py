# Desafio 30 - Par ou ímpar
# Crie um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar.

num = int(input("Insira um número inteiro: "))
n = num % 2
if n == 0:
    print("O número inserido é par!")
else:
    print("O número inserido é ímpar!")
