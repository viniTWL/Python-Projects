from random import shuffle

a = (input('Qual o primeiro aluno irá participar do sorteio?'))
b = (input('Segundo aluno:'))
c = (input('Terceiro aluno:'))
d = (input('Quarto aluno:'))
r = [a, b, c, d]
shuffle(r) # comando para trocar a ordem de forma aleatoria
print('Os alunos foram escolhidos na seguinte ordem {}:'.format(r))





