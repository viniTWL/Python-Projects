def readcash(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).strip().replace(',', '.')
        if entrada.isalpha() or entrada == '':
            print('\033[0;31mERR0! Digite um valor válido\033[m')
        else:
            valido = True
            return float(entrada)



