# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# a)	Abaixo de 18,5: abaixo do peso
# b)	Entre 18,5 e 25: peso ideal
# c)	25 até 30: sobrepeso
# d)	30 até 40: obesidade
# e)	Acima de 40: obesidade mórbida

peso = float(input("Insira seu peso (Kg):  "))
altura = float(input("Insira sua altura (M): "))
imc = peso / (altura ** 2)
print(f"Seu IMC é: {imc:.2f}")
if imc < 18.5:
    print("ABAIXO DO PESO!")
elif imc >= 18.5 and imc <= 25:
    print("PESO IDEAL!")
elif imc > 25 and imc <= 30:
    print("SOBREPESO!")
elif imc > 30 and imc <= 40:
    print("OBESIDADE!")
else:
    print("OBESIDADE MÓRBIDA!")