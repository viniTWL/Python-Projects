print('===== VERIFICANDO UMA P.A USANDO WHILE =====')
pt = int(input('Digite o primeiro termo da P.A:'))
r = int(input('Digite a razão da P.A:'))
termo = pt
cont = 1
tot = 0
mais = 10
while mais != 0:
    tot = tot + mais
    while cont <= tot:
      termo += r
      cont += 1
      print('{} > '.format(termo), end='')
      print('Pausa')
      mais = int(input('Quer mostrar mais quantos termos a mais?'))
print('fim')
