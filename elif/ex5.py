str(print('\033[4;30mVamos calcular a sua média.\033[m'))
a = float(input('Digite o valor da primeira nota:'))
b = float(input('Digite o valor da segunda nota:'))
total = (a+b)/2
if total < 5:
    print('\033[1;31mSua média foi {}, você está reprovado!'.format(total))
elif total <= 6.9:
    print('\033[1;33mSua média foi {}, você está de recuperação!'.format(total))
elif total >= 7:
    print('\033[1;32mSua média foi {}, você está aprovado!'.format(total))







