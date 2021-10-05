print('\033[0;36m======= FRASES PALÍNDROMAS =======\033[m')
frase = str(input('Digite a frase:')).strip().upper()
print('Você digitou a frase {}.'.format(frase))
separado = frase.split() #separei a frase
junto = ''.join(separado) #juntei-as denovo
inverso = ''
for let in range(len(junto)-1, -1, -1):
    inverso += junto[let]
if inverso == junto:
    print('''A frase é {}, invertida ela fica {}.
          É pálindroma.'''.format(frase, inverso))
else:
    print('''A frase é {}, invertida ela fica {}.
              Não é pálindroma.'''.format(frase, inverso))


