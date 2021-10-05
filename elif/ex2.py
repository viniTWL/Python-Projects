str(print('\033[0;35mBem-vindo ao conversor de números! Você poderá escolher entre binário,octal e hexadecimal.\033[m'))
n = int(input('Digite um número:'))
r = int(input('''Para qual base você deseja converter?
Se desejar para Binário, digite 1.
Para Octal, digite 2.
Para Hexadecimal,digite 3:'''))
if r == 1:
    print('{} convertido para Binário é {}.'.format(n, bin(n)))
elif r == 2:
    print('{} convertido para Octal é {}.'.format(n, oct(n)))
elif r == 3:
    print('{} convertido para Hexadecimal é {}.'.format(n, hex(n)))
else:
    print('Opção inválida.')
