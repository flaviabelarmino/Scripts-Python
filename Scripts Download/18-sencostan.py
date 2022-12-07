# Desafio 18 - Seno, cosseno e tangente
# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo

from math import radians, sin, cos, tan
angulo=float(input("Insira o ângulo: "))
seno=sin(radians(angulo))
print(f"O seno de {angulo} tem {seno:.2f}")
cosseno=cos(radians(angulo))
print(f"O cosseno de {angulo} tem {cosseno:.2f}")
tangente=tan(radians(angulo))
print(f"A tangente de {angulo} tem {tangente:.2f}")
