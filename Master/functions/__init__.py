from arquivo import *
from time import sleep
arq = 'registo.txt'
if not archiveExist(arq):
    createArchive(arq)


def register():
    def line():
        print('-' * 40)
    while True:
        line()
        print('MENU PRINCIPAL'.center(40))
        line()
        print('''\033[0;33m1\033[m - \033[0;34mVer pessoas cadastradas
\033[0;33m2\033[m - \033[0;34mCadastrar novas pessoas
\033[0;33m3\033[m - \033[0;34mSair do Sistema\033[m''')
        line()
        while True:
            try:
                opc = int(input('\033[0;33mSua opção:\033[m'))
                if opc == 1:
                    line()
                    print('PESSOAS CADASTRADAS'.center(40))
                    line()
                    readArchive(arq)
                    sleep(1.5)
                    break
                if opc == 2:
                    line()
                    print('NOVO CADASTRO'.center(40))
                    line()
                    while True:
                        nome = str(input('Nome:')).strip()
                        if nome.isnumeric():
                            print('\033[0;31mERRO! Por favor, digite apenas letras!\033[m')
                        else:
                            break
                    while True:
                        try:
                            age = int(input('Idade:'))
                        except:
                            print('\033[0;31mERRO! Por favor, digite apenas números!\033[m')
                        else:
                            sleep(1.5)
                            ArchiveAdd(arq, nome, age)
                            break
                    break
                if opc == 3:
                    line()
                    print('SAINDO DO SISTEMA...'.center(40))
                    break
            except:
                print('\033[0;31mERRO! Por favor digite um número inteiro válido!\033[m')
                line()
            else:
                print('\033[0;31mERRO! Por favor digite um número inteiro válido!\033[m')
                line()
        if opc == 3:
            break

