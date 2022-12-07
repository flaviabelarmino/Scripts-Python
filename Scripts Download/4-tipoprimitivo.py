# Desafio 4
# Faça um programa que leia algo e mostre na tela
# O seu tipo primitivo e todas as informações possíveis sobre ele

a=input('Digite algo: ')
print('O tipo primitivo é: ',type(a))
print(f'Só foram digitados espaços? {a.isspace()}')
print(f'É um número? {a.isnumeric()}')
print(f'É alfabético? {a.isalpha()}')
print(f'É alfanumérico? {a.isalnum()}')
print(f'Está em maiúsculo? {a.isupper()}')
print(f'Está em minúsculo? {a.islower()}')
print(f'Está capitalizada? {a.istitle()}')

