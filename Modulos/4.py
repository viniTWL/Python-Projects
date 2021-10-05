from random import choice

a = str(input('Qual o primeiro aluno irá participar do sorteio?'))
b = str(input('Segundo aluno:'))
c = str(input('Terceiro aluno:'))
d = str(input('Quarto aluno:'))
r = [a, b, c, d] #lista
print('O aluno escolhido foi {}'.format(choice(r)))# comando do modulo random para escolha aleatoria



