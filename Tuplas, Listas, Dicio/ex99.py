from time import sleep
def maior(*nums):
    print('=-'*40)
    print('Analisando os valores passados...')
    sleep(2)
    for i in nums:
        print(i, end=' ', flush=True)
        sleep(0.5)
    print(f'. Foram informados {len(nums)} números ao todo.'
          f' O maior número informado foi {max(nums)}.''')

#PROGRAMA
maior(6, 8, 3, 10, 2)
maior(0)
maior(3, 5, 7)
maior(2, 5)

