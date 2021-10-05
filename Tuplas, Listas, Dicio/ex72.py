nums = ('zero','um', 'dois', 'três', 'quatro', 'cinco', 'seis' , 'sete' , 'oito' , 'nove', 'dez', 'onze', 'doze',
        'treze','quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
r = int(input('Digite um número de 0 a 20 para vê-lo por extenso:'))
while r > 20 or r < 0:
    print('\033[0;31mNúmero inválido, digite novamente.\033[m')
    r = int(input('Digite um número de 0 a 20 para ve-lo por extenso:'))
print(f'Você digitou o número \033[0;32m{nums[r]}.')

