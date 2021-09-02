contas = ['multiplicação, divisão, soma, subtração']
tipo_de_conta = input('Qual conta você quer fazer? ')
numero_user   = int(input('Digite aqui o primeiro número: '))
numero_user2  = int(input('Digite aqui o segundo número: '))

if 'multiplicação' in tipo_de_conta:
    print('O resultado da conta é {}'.format(numero_user * numero_user2))
elif 'divisão' in tipo_de_conta:
    print('O resultado da conta é {}'.format(round(numero_user / numero_user2)))
elif 'soma' in tipo_de_conta:
    print('O resultado da conta é {}'.format(numero_user + numero_user2))
else:
    print('O resultado da conta é {}'.format(numero_user - numero_user2))