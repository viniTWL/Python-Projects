print('Vamos verificar qual é o maior número dentre os 3.')
p = int(input('Digite o primeiro número:'))
s = int(input('Digite o segundo número:'))
t = int(input('Digite o terceiro número:'))
menor = p
if s < p and s < t:
    menor = s
if t < p and t < s:
    menor = t
if s > p and s > t:
    maior = s
if t > s and t > p:
    maior = t
    print('O menor número é o {}'.format(menor))
    print('O maior número é o {}'.format(maior))






