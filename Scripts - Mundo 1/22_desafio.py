#Crie um programa que leia o nome completo de uma pessoa e mostre todas as letras maiúsculas, todas minúsculas,
# quantas letras ao (sem considerar espaços), quantas letras tem o primeiro nome:

nome=str(input("Insira seu nome completo: ")).strip()
print(nome)
print(f"Nome em maiúsculas: {format(nome.upper())}")
print(f"Nome em minúsculas: {format(nome.lower())}")
print(f"Seu nome tem {format(len(nome)-nome.count(' '))} letras")
#print(f"Seu primeiro nome tem {format(nome.find(' '))} letras")
separa=nome.split()
print(f"Seu primeiro nome é {format(separa[0])}, e tem {len(separa[0])} letras")