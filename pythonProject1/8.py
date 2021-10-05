p = input('Qual produto você deseja?')
v = float(input('Qual o preço do produto?R$'))
t = float(v*0.05)
print('Este {} está com 5% de promoção! Agora ele custa R${:.2f}.'.format(p, v-t))






