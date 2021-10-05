v = (int(input('Digite o número da tabuada:')))
num = v
for v in range(0, 11):
    print('{} x {} = {}'.format(num, v, num*v))
print('\033[0;33mEssa é a tabuada de {}!'.format(num))