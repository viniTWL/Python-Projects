print('\033[0;32m===== BRASILEIRÃO 2014 =====\033[m')
lista = ('Cruzeiro', 'São Paulo', 'Internacional', 'Corinthians', 'Atlético-MG', 'Fluminese','Grêmio','Athletico-PR',
         'Santos','Flamengo','Sport','Goiás','Figueirense','Coritiba','Chapecoense','Palmeiras','Vitória','Bahia',
         'Botafogo','Críciuma')
while True:
    print('Selecione a opção desejada:')
    r = int(input('''[1] Ver a tabela completa
[2] Ver apenas quais se classificaram para a libertadores
[3] Apenas quais foram os rebaixados apenas
[4] Apenas qual foi o campeão
[5] Lista dos Times em Ordem Alfabética
[0] Finalize o programa
\033[0;32mOpção:\033[m'''))
    if r == 1:
        for c in lista:
            print(c)
    elif r == 2:
        print(lista[:5])
    elif r == 3:
        print(lista[16:])
    elif r == 4:
        print(lista[0])
    elif r == 5:
        print(sorted(lista))
    elif r == 0:
        break
    else:
        print('Opção Inválida')
    print('-----------------------------------------------------------')
print('PROGRAMA FINALIZADO')
