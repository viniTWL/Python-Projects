print('Vamos analisar se as 3 retas formam um triangulo.')
a = float(input('Digite o valor da primerira reta:'))
b = float(input('Digite o valor da segunda reta:'))
c = float(input('Digite o valor da terceira reta:'))
if a < b + c and b < a + c and c < a +b:
    print('\033[0;32mEsses valores formam um triângulo.', end=' ')
    if a == b == c:
        print('Esse triângulo é equilatero.')
    elif a != b != c != a:
        print('Esse triângulo é escaleno.')
    elif:
        print('Esses valores não formam um triângulo.')
    else:
        print('Esse triângulo é isósceles .')