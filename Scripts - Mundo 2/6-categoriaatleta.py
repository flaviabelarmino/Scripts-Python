#Desafio 6 - Categoria idade atleta
#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e
# mostre sua categoria, de acordo com a idade:
#a)	Até 9 anos: MIRIM
#b)	Até 14 anos: INFANTIL
#c)	Até 19 anos: JUNIOR
#d)	Até 20 anos: SÊNIOR
#e)	Acima: MASTER

from datetime import date
atual = date.today().year
idade = int(input("Insira o ano de nascimento do atleta: "))
id = atual-idade
print(f"Você tem {id} anos")
if id <= 9:
    print("É atleta é da categoria: MIRIM")
elif id >= 10 and id <= 14:
    print("É atleta é da categoria: INFANTIL")
elif id >= 15 and id <= 19:
    print("É atleta é da categoria: JUNIOR")
elif id == 20:
    print("É atleta é da categoria: SÊNIOR")
else:
    print("É atleta é da categoria: MASTER")