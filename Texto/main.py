nome=str(input('Digite seu nome completo:')).strip()
print('\033[1;32mAnalisando seu nome...\033[m')
print('Seu nome em maiusculo é:\033[0;34m{}\033[m'.format(nome.upper()))
print('Seu nome em minusculo é:\033[0;34m{}\033[m'.format(nome.lower()))
print('Seu nome tem {} letras.'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras.'.format(nome.find(' ')))

























