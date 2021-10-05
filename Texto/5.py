fr = str(input('Digite uma frase:')).upper().lstrip().rstrip() #abreviando pela esquerda e direita
c = fr.count('A') #contando o numero de vezes que a aparece
print('A letra A aparece {} vezes na frase.'.format(c))
print('A letra A apareceu pela primeira vez na posição {}'.format(fr.find('A')+1))
print('A letra A apareceu pela ultima vez na posição {}'.format(fr.rfind('A')+1))
# o +1 se deve ao fato da primeira posição sempre ser 0





