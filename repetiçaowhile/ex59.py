op = 99
print('\033[1;35m===== MENU DE OPÇÕES =====\033[m')
a = int(input('Digite o primeiro número:'))
b = int(input('Digite o segundo número:'))
while op != 7:
   op = int(input('''Selecione a opção desejada:
[1] Somar
[2] Subtrair
[3] Dividir
[4] Multiplicar
[5] Maior Número
[6] Novos Números
[7] Sair do Programa
- Qual é a sua opção?'''))
   if op == 1:
       print('\033[0;32mA soma dos números é\033[m',a + b)
       print('----------------------------')
   elif op == 2:
       print('\033[0;32mA subtração dos números é\033[m',a - b)
       print('----------------------------')
   elif op == 3:
       print('\033[0;32mA divisão dos números é\033[m',a / b)
       print('----------------------------')
   elif op == 4:
       print('\033[0;32mA multiplicação dos números é\033[m', a * b)
       print('----------------------------')
   elif op == 5:
       if a > b:
           print('\033[0;32m{} é o maior número.\033[m'.format(a))
           print('----------------------------')
       elif b > a:
           print('\033[0;32m{} é o maior número.\033[m'.format(b))
           print('----------------------------')
   elif op == 6:
       a = int(input('Digite o primeiro número:'))
       b = int(input('Digite o segundo número:'))
   elif op == 7:
       print('\033[0;31m===== Fim do programa =====')
   else:
       print('\033[0;31mDIGITE UM NÚMERO VALIDO.\033[m')
       print('----------------------------')





