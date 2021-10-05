cores = {'blue':'\033[0;30;44m',
         'white':'\033[0;30;40m',
         'green':'\033[0;30;42m'}
def ajuda():
    cores = {}
    while True:
        print('\033[0;30;42m~' * 30)
        print('   SISTEMA DE AJUDA PyHELP')
        print('~' * 30)
        r = str(input('\033[mFunção ou Biblioteca >')).strip().lower()
        if r == 'fim':
            print('\033[7;31;40m----- PROGRAMA FINALIZADO -----')
            break
        else:
            print('\033[0;30;44m~' * 40)
            print(f'   ACESSANDO O MANUAL DO COMANDO "{r}"')
            print('~'*40)
            print('\033[7;30m')
            print(help(r))


#PROGRAMA
ajuda()