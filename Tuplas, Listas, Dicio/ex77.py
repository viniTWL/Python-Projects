print('=== IDENTIFICANDO VOGAIS =====')
words = ('Computador', 'Programaçao', 'Cadeira', 'Mousepad', 'Fone')
vogais = ('a', 'e', 'i', 'o', 'u')
for c in words:
    print(f'\nNa palavra {c} temos', end=' ')
    for v in c:
        if v.lower() in 'aeiou':
            print(v, end='')
