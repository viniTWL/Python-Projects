cont = 0
res = 0
import random
print('\033[1;32m===== TENTE ACERTAR O NÚMERO QUE O COMP PENSOU =====\033[m')
ran = random.randint(1, 5) #computador está randomizando
while res != ran:
    res = int(input('Digite um numéro de 1 a 5:'))#tentando adivinhar
    cont = cont + 1
    ran = random.randint(1, 5)  #randomizando novamente, pois a res foi errada
    print('O COMP pensou no número \033[1;32m{}\033[m.'.format(ran))
print('\033[1;32mVOCÊ ACERTOU!')
print('Você precisou de {} tentativas para acertar.'.format(cont))







