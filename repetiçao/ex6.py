tot = 0
print('======== VERIFICAR SE O NÚMERO É PRIMO ========')
num = int(input('Digite um número inteiro:'))
for c in range(1, num+1):
    if num % c == 0:
        print('\033[0;31m')
        tot = tot + 1
    else:
        print('\033[0;32m')
        tot + 1
if tot == 2:
    print('O número foi dividido {} vezes, por isso é primo.'.format(tot))
elif tot >= 3:
    print('O número foi dividido {} vezes, por isso não é primo.'.format(tot))
