num = int(input("Insira um número inteiro: "))
#três aspas para conseguir fazer várias linhas de uma só vez
print('''Escolha uma das bases para conversão:
[1] Binário
[2] Octal
[3] Hexadeximal''')
opcao = int(input("Insira sua opção: "))
if opcao == 1:
    #[2:] significa o fatiamento de string (da posição 0 a 1 não aparecerá, somente a partir da posição 2
    print(f"Convertido para Binário: {bin(num)[2:]}")
elif opcao == 2:
    print(f"Convertido para Octal: {oct(num)[2:]}")
elif opcao == 3:
    print(f"Convetido para Hexadecimal: {hex(num)[2:]}")
else:
    print("Base inexistente! Reinicie o programa!")