sex = str(input('Digite seu sexo [M/F]:')).upper().strip()
while sex != 'F' and sex != 'M':
    print('\033[0;33mDIGITE UMA OPÇÃO VÁLIDA!\033[m')
    sex = str(input('Digite seu sexo [M/F]:')).upper().strip()
print('OK')