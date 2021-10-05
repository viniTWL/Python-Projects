aluno = dict()
aluno['nome'] = str(input('Nome Completo:'))
nota1 = float(input('Digite a nota da Primeira prova:'))
nota2 = float(input('Digite a nota da Segunda Prova:'))
aluno['média'] = (nota1 + nota2) / 2
if aluno['média'] < 5:
    aluno['situação'] = 'Reprovado'
if aluno['média'] >= 5:
    aluno['situação'] = 'Recuperação'
if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'
for k, v in aluno.items():
    print(f'A {k} é {v}. ')
