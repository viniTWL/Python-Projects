str(print('\033[0;30mCalcule seu IMC.\033[m'))
a = float(input('Qual a sua altura?'))
p = float(input('Qual o seu peso?'))
i = int(input('Qual a sua idade?'))
res = p/a**2
if res < 18.5:
    print('\033[0;33mO seu IMC é de {:.1f}.Você está abaixo do peso.'.format(res))
elif res <= 25:
    print('\033[0;32mO seu IMC é de {:.1f}.Você está no peso ideal.'.format(res))
elif res <= 30:
    print('\033[0;33mO seu IMC é de {:.1f}.Você está com sobrepeso.'.format(res))
elif res >= 40:
    print('\033[0;31mO seu IMC é de {:.1f}.Você está com obesidade.'.format(res))


