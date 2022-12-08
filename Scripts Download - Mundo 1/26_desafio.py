#Faça um programa que leia uma frase pelo teclado e mostre:
#a)	Quantas vezes aparece a letra “A”.
#b)	Em que posição ela aparece a primeira vez
#c)	Em que posição ela aparece a última vez

a = str(input("Insira uma frase: ")).upper().strip()
print("A letra 'A' aparece: ",a.count('A'), "vezes")
print("A letra 'A' aparece pela primeira vez na posição: ", a.find('A')+1)
print("A letra 'A' apareceu na posição: ", a.rfind('A')+1)