somaidade = 0
oldest = 0
nameoldest = 0
mulher = 0
print('======= ANALISADOR DE DADOS =======')
for c in range(1, 5):
    print('{}ª Pessoa'.format(c))
    nome = str(input('Qual o seu nome?')).strip()
    idade = int(input('Qual a sua idade?'))
    gen = input('''Qual seu genêro?
Masculino[M]
Feminino[F]
Outro[O]
- Digite a opção:'''.strip().upper())
    somaidade = somaidade + idade/4
    if c == 1 and gen in 'Mm':
        oldest = idade
        nameoldest = nome
    if gen in 'Mm' and idade > oldest:
        oldest = idade
        nameoldest = nome
    if gen in 'Ff' and idade < 20:
        mulher = mulher + 1
print('A média de idade dessas 4 pessoas é de {:.1f} anos.'.format(somaidade))
print('O homem mais velho tem {} anos e se chama {}.'.format(oldest, nameoldest))
print('Possui {} mulher com menos de 20 anos.'.format(mulher))










