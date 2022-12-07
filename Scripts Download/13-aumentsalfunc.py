# Desafio 13
# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento

salfunc=float(input("Insira o salário do funcionário R$: "))
aumento=(salfunc*15)/100
print("Você teve aumento de 15% no seu salário!")
print("------------------------------------------")
print(f"Você receberá R$: {salfunc+aumento:.2f}")
print("------------------------------------------")
