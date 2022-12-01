#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo,
# calcule e mostre o comprimento da hipotenusa

from math import hypot
catop=float(input("Insira o comprimento do cateto oposto: "))
catadj=float(input("Insira o comprimento do cateto adjacente: "))
hipotenusa=hypot(catop,catadj)
print(f"A hipotenusa possui {hipotenusa:.2f} comprimento.")