a = int(input('Digite o primeiro número:'))
b = int(input('Digite o segundo número:'))
c = int(input('Digite o terceiro número:'))
d = int(input('Digite o quarto número:'))
nums = (a, b, c, d)
print(f'Você digitou os números {nums}.')
print(f'O número 9 apareceu {nums.count(9)} vezes.')
if 3 in nums:
    print(f'O número 3 foi digitado pela primeira vez na posição {nums.index(3) + 1}')
else:
    print('Não houve nenhum número 3.')
print(f'Os números pares digitados foram ', end=' ')
for par in nums:
    if par % 2 == 0:
        print(par, end='')



