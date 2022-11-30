#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade
# de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².

largura=float(input("Insira a largura da parede em metros: "))
altura=float(input("Insira a altura da parede em metros: "))

area=largura*altura
tinta=area/2
print(f"\nÁrea da parede: {area:.2f} m²")
print(f"Quantidade de tinta utilizada: {tinta:.1f} l")