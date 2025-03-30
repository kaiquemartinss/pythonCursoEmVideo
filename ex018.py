import math
from math import radians

angulo_graus = float(input('Digite um ângulo que você deseja: '))
angulo_radianos = math.radians(angulo_graus)
seno = math.sin(angulo_radianos)
cosseno = math.cos(angulo_radianos)
tangente = math.tan(angulo_radianos)
print(f'O ângulo de {angulo_graus} tem o SENO de {seno:.2f}')
print(f'O ângulo de {angulo_graus} tem o COSSENO de {cosseno:.2f}')
print(f'O ângulo de {angulo_graus} tem a TANGENTE de {tangente:.2f}')