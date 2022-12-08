# – Crie um programa que leia o nome de uma pessoa e diga se ela tem “Silva” no nome.

nome = str(input("Insira seu nome completo: ")).strip().lower().split()
print("Seu nome tem Silva? ",'silva' in nome)