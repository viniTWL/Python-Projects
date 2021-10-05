tot = 0
num = int(input('Digite o número:'))
for i in range(1, num+1):
    if num % i == 0:
        print('\033[0;32m')
        tot += 1
    else:
        print('\033[0;33m')
print('O número {} foi dividido {] vezes.'.format(num, tot))
if tot == 2:
    print('O número é primo')
else:
    print('Não é primo')
