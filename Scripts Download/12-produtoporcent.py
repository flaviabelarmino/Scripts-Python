# Desafio 12 - Desconto de produto
# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

p=float(input("Insira o preço do produto R$: "))
desconto=(p*5)/100
pagar=p-desconto
print("\nVocê possui 5% de desconto!")
print("______________________________")
print(f"Valor a pagar: {pagar:.2f}")
print("______________________________")
