# Verificar letras
# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome “Santo”.

cid = str(input("Insira o nome da cidade: ")).strip().split()
print(cid[0].upper() == 'SANTO')
