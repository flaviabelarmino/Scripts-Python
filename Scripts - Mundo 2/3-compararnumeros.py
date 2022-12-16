#Desafio 3 - Comparar números
#Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
#a)	O primeiro valor é maior
#b)	O segundo valor é maior
#c)	Não existe valor maior, os dois são iguais

n1 = int(input("Insira o 1º valor: "))
n2 = int(input("Insira o 2º valor: "))
#Inseri cores para dar destaque
if n1 > n2:
    print("\33[0;35mO primeiro valor é maior!")
elif n2 > n1:
    print("\33[0;34mO segundo valor é maior!")
else:
    print("\33[0;33mNão existe valor maior, os dois são iguais!")
