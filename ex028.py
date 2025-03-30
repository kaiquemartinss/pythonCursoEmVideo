from random import randint
from time import sleep
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
ncomp = randint(0, 5)
num = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(3)
if num == ncomp:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print(f'GANHEI! Pensei no número {ncomp} e não no {num}!')