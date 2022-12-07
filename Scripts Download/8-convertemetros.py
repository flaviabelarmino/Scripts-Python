# Desafio 8 
# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

num=float(input('Insira um valor em metros: '))
print(f'km: {num/1000}')
print(f'hm: {num/100}')
print(f'dam: {num/10}')
print(f'dm: {num*10}')
print(f'cm: {num*100}')
print(f'mm: {num*1000}')
