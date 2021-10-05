
Marcio Coelho
há 1 ano (editado)
Vários testes contra "bugs" e aplicando as soluções depois, resultou nisso. Se o usuário der enter em qualquer das respostas, colocar espaço ou qualquer outra string inválida, digitar valor que não seja inteiro ou flutuante, colocar vírgula ao invés de ponto para uso de decimais, repetir o número, etc... mas, se acharem qualquer outro defeito que pare o programa, avisem.
Edit: Pequena alteração no código. Esqueci dos números negativos. Agora também podem ser usados números negativos sem "crash".

# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.


more = 0
values = list()
number_type = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', '-')
while more == 0:
    restart = 0
    stop = ''
    value = (input('Digite um número para adicionar na lista '
                   '(\33[1:33mPROIBIDO\33[m repetir número): '))
    if value == '':
        print(f'\33[1:31mERRO!\33[m Digite apenas números. '
                  f'Use "." para os decimais e "-" para negativos.')
        continue
    for char in value:
        if char == '-' and (value.count('-') > 1 or value.index('-') != 0):
            print(f'\33[1:31mERRO!\33[m Digite apenas números. '
                      f'Use "." para os decimais e "-" para negativos.')
            restart = 1
            break
        if all(char != number for number in number_type):
            print(f'\33[1:31mERRO!\33[m Digite apenas números. '
                      f'Use "." para os decimais e "-" para negativos.')
            restart = 1
            break
    if restart == 1:
        continue
    values.append(float(value))
    if values.count(values[-1]) > 1:
        print(f'\33[1:31mREPETIDO!\33[m Número {values[-1]} já existe na lista.')
        values.pop()
    else:
        print(f'Número {values[-1]} adicionado com \33[1:34mSUCESSO!\33[m')
        while stop[:1].lower() not in 'sn' or stop == '':
            stop = str(input('Deseja adicionar mais números a lista? (s/n): '))
            if stop[:1].lower() not in 'sn' or stop == '':
                print('\33[1:31mERRO!\33[m Opção inválida. '
                          'Digite "s" (sim) para continuar ou "n" (não) para mostrar o resultado.')
            elif stop[:1].lower() == 'n':
                more = 1
print('Os números digitados (sem repetição) em ordem crescente são: ' if len(values) > 1
          else 'O número digitado (sem repetição) é: ', end='')
for pos, item in enumerate(sorted(values)):
    print(f'{item}, ' if pos < len(values) - 2
              else f'{item} e ' if pos < len(values) - 1
              else f'{item}.', end='')