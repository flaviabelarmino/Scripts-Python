# Desafio 35 - Analisar triângulo
# Desenvolva um programa que leia o comprimento de três retas e
# diga ao usuário se elas podem ou não formar um triângulo.

r1 = float(input("Insira a reta 1: "))
r2 = float(input("Insira a reta 2: "))
r3 = float(input("Insira a reta 3: "))
print("-----Analisador de triângulo!-----")
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("As retas podem formar triângulo!")
else:
    print("As retas não formam trinângulo!")