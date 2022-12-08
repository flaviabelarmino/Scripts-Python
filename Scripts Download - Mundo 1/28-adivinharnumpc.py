# Desafio 28 - Adivinhar número PC
# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e
# peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
pc = randint(0, 5)
print("Eu, o computador, pensei em um número, sabe qual é?")
num = int(input("Digite um número entre 0 e 5 para adivinhar: "))
print("-=-"*16)
if num == pc:
    print("Parabéns! Você acertou!")
else:
    print(f"Que pena, você errou! Eu pensei no número {pc}.")
