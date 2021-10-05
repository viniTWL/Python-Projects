print('{:^40}'.format('\033[0;33mSITE DA REDE DE COMPUTADORES MONTADOS DO VINI\033[m'))
pre = float(input('Qual é o preço do produto?R$'))
print('A sua compra está custando R${}, vamos dar uma olhada nas condições de pagamento...'.format(pre))
print('''Há 4 opções de pagamento:
Para pagar à vista no dinheiro/cheque com 10% de desconto, digite "1".
Para pagar à vista no cartão com 5% de desconto, digite "2".
Para pagar em até 2x no cartão sem descontos, digite "3".
Para pagar em 3x ou mais no cartão, com 20% de Juros, digite "4".''')
r = int(input('Selecione sua opção:'))
if r == 1:
    tot = pre - (pre * 0.1)
    print('Você escolheu a opção 1, e o preço final é de R${:.2f}.'.format(tot))
elif r == 2:
    tot = pre - (pre*0.05)
    print('Você escolheu a opção 2, e o preço final é de R${:.2f}.'.format(tot))
elif r == 3:
    tot = pre
    par = tot/2
    print('Você escolheu a opção 3, e o preço final é de R${:.2f}.'.format(tot))
    print('Será dividido em 2x de {:.2f}'.format(par))
elif r == 4:
    p = int(input('Você irá dividir em quantas parcelas?'))
    tot = pre + (pre*0.2)
    par = tot/p
    print('Você escolheu a opção 4, e o preço final é de R${:.2f}.'.format(tot))
    print('Será dividido em {}x de {:.2f}.'.format(p, par))
else:
    print('\033[0;31mOPÇÃO INVÁLIDA DE PAGAMENTO.')