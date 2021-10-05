def archiveExist(name):
    try:
        a = open(name, 'rt')
        a.close()

    except FileNotFoundError:
        return False
    else:
        return True

def createArchive(name):
    try:
        a = open(name, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo!')
    else:
        print('Arquivo criado com sucesso!')


def readArchive(name):
    try:
        a = open(name, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        for tab in a:
            dado = tab.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')

def ArchiveAdd(arq, nome='desconhecido', age= 0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um erro na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome};{age}\n')
        except:
            print('Houve um erro ao escrever dados!')
        else:
            print(f'\033[0;32mNovo registro de {nome} adicionado com sucesso!\033[m')
        finally:
            a.close()

