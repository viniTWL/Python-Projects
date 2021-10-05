print('=========== 10 TERMOS DE UMA P.A ============')
t = int(input('Digite o primeiro termo da sua P.A:'))
r = int(input('Digite a Razão da P.A:'))
d = t + 9 * r # chegar ao ultimo termo da pa
for pa in range(t, d+r, r): #d+r pois precisa chegar no ultimo termo
    print(pa, end='>')
print('Acabou')