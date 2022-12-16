#Desafio 5 - Média aluno
#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
#a)	Média abaixo de 5.0: REPROVADO
#b)	Média entre 5.0 e 6.9: RECUPERAÇÃO
#c)	Média 7.0 ou superior: APROVADO

n1 = float(input("Insira a primeira nota: "))
n2 = float(input("Insira a segunda nota: "))
media=(n1+n2)/2
#Inseri cores para ficar mais visível as notas
if media < 5.0:
    print(f"\033[1;31mAluno REPROVADO! Média final {media}")
elif media <= 6.9 and media >= 5.0:
    print(f"\033[1;33mAluno em RECUPERAÇÃO! Média final: {media}")
elif media <= 10.0 and media >= 7.0:
    print(f"\33[1;32mAluno APROVADO! Média final: {media}")
else:
    print("Nota inexistente!")