# Desafio 34 - Aumento funcionário
# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$ 1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

sal = float(input("Qual o valor do seu salário? "))
if sal > 1250:
    aumento = sal*10/100
    print(f"Você tem um aumento de 10% = R$ {aumento:.2f}. Total a receber R$ {sal+aumento:.2f}")
elif sal <= 1250:
    aume = sal*15/100
    print(f"Você tem um aumento de 15% = R$ {aume:.2f}. Total a receber R$ {sal+aume:.2f}")