#Desafio 1 - Empréstimo casa
#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
#O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

print("Olá, seja bem-vindo(a) ao banco Emprestar!")
print("\33[1;33m******************************************\33[m")
casa = float(input("Insira o valor da casa R$: "))
sal = float(input("Insira o salário do comprador R$: "))
tempo = int(input("Insira em quantos anos o valor será pago R$: "))
trinta_porc = sal*30/100
mes = tempo*12
parcela = casa/mes
print("\33[1;33m*******************************************\33[m")
if parcela > trinta_porc:
    print(f"\33[1;41mEmpréstimo negado! Valor excede 30% do salário! Valor da parcela mensal R$: {parcela:.2f}\33[m")
else:
    print(f"\33[1;42mEmpréstimo aprovado! Aproveite a compra! Valor da parcela mensal R$: {parcela:.2f}\33[m")
