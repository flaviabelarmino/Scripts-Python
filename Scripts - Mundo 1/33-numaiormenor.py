# Desafio 33 - Maior e menor
# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = int(input("Insira o primeiro valor: "))
n2 = int(input("Insira o segundo valor: "))
n3 = int(input("Insira o terceiro valor: "))

# Testando maior valor
if n1 > n2 and n1 > n3:
        print(f"O maior valor: {n1}")
elif n2 > n1 and n2 > n3:
        print(f"O maior valor: {n2}")
elif n3 > n1 and n3 > n2:
        print(f"O maior valor: {n3}")

# Testanto menor valor
if n1 < n2 and n1 < n3:
    print(f"O menor valor: {n1}")
elif n2 < n1 and n2 < n3:
    print(f"O menor valor: {n2}")
elif n3 < n1 and n3 < n2:
    print(f"O menor valor: {n3}")
