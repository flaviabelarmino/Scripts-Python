# Desafio 32 - Ano bissexto
# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

from datetime import date
ano = int(input("Insira um ano: "))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f"{ano} é ano bissexto! ")
else:
    print(f"{ano} não é ano bissexto")