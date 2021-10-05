def readINT(msg):
    while True:
        try:
            i = int(input(msg))
        except KeyboardInterrupt:
            print('O usuário preferiu não informar o valor.')
            i = 0
            break
        except:
            print('\033[0;31mERRO! Por favor, digite um número real válido.\033[m')
            continue
        else:
            return i


def readfloat(msg):
    while True:
        try:
            r = float(input(msg))
        except KeyboardInterrupt:
            print('O usuário preferiu não informar o valor.')
            r = 0
            break
        except:
            print('\033[0;31mERRO! Por favor, digite um número real válido.\033[m')
            continue
        else:
            return r


#PROGRAMA
numi = readINT('Digite o número inteiro:')
numr = readfloat('Digite o número real:')
print(f'O usuário digitou o valor inteiro {numi} e o real {numr}')