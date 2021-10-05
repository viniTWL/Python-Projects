def ficha(j, g):
    if not j:
        j = '<desconhecido>'
    if not g:
        g = 0
    print(f'O jogador {j} fez {g} gols no total.')


#Programa
j = str(input('Qual o nome do seu jogador?')).strip()
g = str(input(f'Quantos gols {j} fez?')).strip()
if g.isnumeric():
    g = int(g)
else:
    g = 0
(ficha(j, g))