from random import randint
print('\033[1;34mBORA JOGAR JOKENPÔ!\033[m')
#\033[0;31m vermelho \033   [0;32m verde \033[0;33m amarelo \033[m
lista = ('Pedra', 'Papel' , 'Tesoura')
comp = randint(0, 2)
print('''Selecione sua opção:
[0] Pedra
[1] Papel
[2] Tesoura''')
jog = int(input('Opção:'))
print('O Comp jogou {}.'.format(lista[comp]))
print('Você jogou {}.'.format(lista[jog]))
if comp == 0:
    if jog == 0:
        print('\033[0;33mEmpatou!')
    elif jog == 1:
        print('\033[0;32mVocê ganhou!')
    elif jog == 2:
        print('\033[0;31mVocê perdeu!')
    else:
        print('Selicione uma opção válida.')
if comp == 1:
    if jog == 1:
        print('\033[0;33mEmpatou!')
    elif jog == 2:
        print('\033[0;32mVocê ganhou!')
    elif jog == 0:
        print('\033[0;31mVocê perdeu!')
    else:
        print('Selecione uma opção válida.')
if comp == 2:
    if jog == 2:
        print('\033[0;33mEmpatou!')
    elif jog == 0:
        print('\033[0;32mVocê ganhou!')
    elif jog == 1:
        print('\033[0;31mVocê perdeu!')
    else:
        print('\033[0;31mSelicione uma opção válida.')





#print(lista[comp])





