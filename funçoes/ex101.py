def vote(ano):
    from datetime import date
    v = date.today().year - ano
    if v >= 18 and v < 70:
        return f'Você tem {v} anos. Seu voto é obrigatório.'
    elif v <= 15:
        return f'Você tem {v} anos. Seu voto não é obrigatório.'
    elif v > 70:
        return f'Você tem {v} anos. Seu voto é opcional.'
    elif v == 16 or v == 17:
        return f'Você tem {v} anos. Tem o direito de voto, mas não é obrigatório.'


#PROGRAMA


born = int(input('Em que ano você nasceu?'))
print(vote(born))


