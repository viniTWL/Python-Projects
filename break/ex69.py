from time import sleep
mi = men = women = 0
print('===== CADASTRO DE PESSOAS =====')
while True:
    print('>>>> Faça o cadastro')
    i = int(input('Digite a idade:'))
    s = str(input('Digite o sexo:[M/F]')).strip().upper()
    while s not in 'MF':
        s = str(input('Digite o sexo:[M/F]')).strip().upper()
    if i >= 18:
        mi += 1
    if s == 'M':
        men += 1
    if s == 'F' and i >= 20:
        women += 1
    r = str(input('Quer continuar cadastrando?[S/N]')).strip().upper()
    while r not in 'SN':
        r = str(input('Quer continuar cadastrando?[S/N]')).strip().upper()
    if r == 'S':
        print('-'*30)
    elif r == 'N':
        break
print('\033[0;32mAnalisando os dados... Processando...\033[m')
sleep(3)
print(f'''De acordo com os dados:
{mi} pessoas possuem mais de 18 anos.
Foram cadastrados {men} homens.
{women} mulheres tem mais de 20 anos.''')
print('\033[1;31m===== FIM DO PROGRAMA =====')


