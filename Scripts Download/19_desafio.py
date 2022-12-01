#Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido

from random import choices
a1=input("Aluno 1: ")
a2=input("Aluno 2: ")
a3=input("Aluno 3: ")
a4=input("Aluno 4: ")
aluno=[a1, a2, a3, a4]
sorteio=choices(aluno)
print(f"O aluno sorteado foi: {sorteio}")