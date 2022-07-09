print("[1] Para multiplicação\n[2] Para divisão\n[3] Para soma\n[4] Para subtração")
tipo_de_conta = int(input('Qual conta você quer fazer? '))
n1 = int(input('Digite aqui o primeiro número: '))
n2 = int(input('Digite aqui o segundo número: '))

if tipo_de_conta == 1:
    print('O resultado da conta é {}'.format(n1 * n2))
elif tipo_de_conta == 2:
    print('O resultado da conta é {}'.format(n1/n2))
elif tipo_de_conta == 3:
    print('O resultado da conta é {}'.format(n1 + n2))
elif tipo_de_conta == 4:
    print('O resultado da conta é {}'.format(n1 - n2))
