import math
oposto = float((input('Cateto oposto: ')))
adjacente = float((input('Cateto adjacente: ')))
hypotenusa = math.hypot(oposto,adjacente)
print(f'O valor da hypotenusa é {hypotenusa:.2f}')

