def notas(sit=False):
    """O programa serve para ler a nota de vários alunos e definir qual a maior nota, a menor nota, a media, e a situação
    da turma.
    O usúario poderá escolher se quer mostrar a situação da tumra, por meio de 'sit=False': Não mostra. 'sit=True: Mostra
    Se o usuário não responder as perguntas com Sim ou Não, o programa notificará uma mensagem de erro."""
    dic = dict()
    lista = list()
    cont = 0
    while True:
        lista.append(float(input('Digite a nota dos alunos:')))
        cont += 1
        dic['total'] = len(lista)
        dic['maior'] = max(lista)
        dic['menor'] = min(lista)
        dic['media'] = sum(lista) / len(lista)
        r = str(input('Quer continuar?[S/N]')).strip().lower()
        if r in 's':
            print('-' * 35)
        if r in 'n':
            break
        while r not in 'nNsS':
            print('DIGITE UM VALOR VÁLIDO')
            r = str(input('Quer continuar?[S/N]')).strip().lower()
            if r in 's':
                print('-' * 35)
            if r in 'n':
                break
    if sit == False:
        print('-'*80)
        print(dic)
    if sit == True:
        print('-' * 80)
        if dic['media'] >= 4:
            dic['situaçao'] = 'Ruim'
        if dic['media'] > 4 and dic['media'] <= 6.5:
            dic['situaçao'] = 'Razoavel'
        if dic['media'] > 6.5 and dic['media'] <= 8.5:
            dic['situaçao'] = 'Boa'
        if dic['media'] > 8.5:
            dic['situaçao'] = 'Excelente'
        print(dic)
    print('----- PROGRAMA FINALIZADO -----')


#PROGRAMA
res = str(input('Quer mostrar a situação da turma ao final do programa?[S/N]')).strip()
while res not in 'sSnN':
    print('DIGITE UM VALOR VÁLIDO')
    res = str(input('Quer mostrar a situação da turma?[S/N]')).strip()
print('-'*60)
if res in 'sS':
    notas(sit=True)
if res in 'nN':
    notas(sit=False)



