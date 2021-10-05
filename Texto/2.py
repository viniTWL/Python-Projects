n = (input('Digite um número de 4 digitos:'))
num = str(n) #coloquei o valor como string para colocar a posição que os números aparecem respectivamente
print('\033[0;31mUnidade:\033[m{}'.format(num[3]))
print('\033[0;32mDezena:\033[m{}'.format(num[2]))
print('\033[0;33mCentena:\033[m{}'.format(num[1]))
print('\033[0;34mMilhar:\033[m{}'.format(num[0]))