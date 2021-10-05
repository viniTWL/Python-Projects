listagem = ('Pão', 11.99,
            'Pão de Queijo', 14.00,
            'Rosquinha', 18.90,
            'Broa Sal', 13.99,
            'Broa doce', 13.99,
            'Biscoito Farinha', 12.00)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}')
    else:
        print(f'R${listagem[pos]:>15}')

