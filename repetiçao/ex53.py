fr = str(input('Digite uma frase:')).strip().upper()
palavra = fr.split() #separando a frase em cada palavra
junto = ''.join(palavra) #juntando a frase novamente, agora sem espaços
inv = ''
for let in range(len(junto)-1, -1, -1):
    inv += junto[let]
if junto == inv:
    print('Você digitou a frase {}, e ao contrário fica {}, É \033[0;32mPALÍNDROMA!'.format(fr, inv))
else:
    print('Você digitou a frase {}, e ao contrário fica {}, NÃO É \033[0;32mPALÍNDROMA!'.format(fr, inv))