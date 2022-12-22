# Desafio 4 - Alistamento militar
#4 – Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade
#(Seu programa também deverá mostrar o tempo que falta ou que passou do prazo):
#a)	Se ele ainda vai se alistar ao serviço militar
#b)	Se é a hora de se alistar
#c)	Se já passou do tempo do alistamento

from datetime import date
#para pegar o ano atual e o dia que o programa está sendo usado
atual = date.today().year
sexo = int(input("Insira 1 para sexo masculino ou 2 para sexo feminino: "))
if sexo == 1:
   print("Sexo masculino!")
   nasc = int(input("Insira seu ano de nascimento: "))
   idade = atual - nasc
   x = nasc + 18
   print(f"Você nasceu em {nasc}.Você tem {idade} ano(s) em {atual}.")
   if idade < 18:
      tmp1 = 18 - idade
      print(f"\33[1;33mVocê ainda irá se alistar, falta(m) {tmp1} anos!\33[m\n"
            f"\33[1;30;43mSeu alistamento será em: {x}.\33[m")
   elif idade == 18:
      print(f"\33[1;30;41mAtenção!!! Já está na hora de você se alistar!\33[m")
   else:
      tmp2 = idade - 18
      print(f"\33[1;34mJá passou seu tempo de se alistar, se passaram {tmp2} anos!\33[m\n"
            f"\33[1;30;44mSeu alistamento foi em: {x}\33[m")
elif sexo == 2:
   print("Sexo feminino! Você não precisa fazer alistamento militar obrigatório!")
else:
   print("Valor desconhecido, reinicie o programa!")