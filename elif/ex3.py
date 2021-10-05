str(print('\033[0;33mVamos ver qual dos dois números é o maior!\033[m'))
um = int(input('Digite o primeiro número:'))
dois = int(input('Digite o segundo número:'))
print('Você digitou o número \033[0;35m{}{}\033[m.'.format(um,dois))
if um > dois:
    print('O primeiro número é o maior.')
elif um < dois:
    print('O segundo número é o maior.')
elif um == dois:
    print('Não existe valor maior. Os números são iguais.')

