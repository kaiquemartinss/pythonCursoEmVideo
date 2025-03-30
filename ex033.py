n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
n3 = int(input('Terceiro valor: '))
""""menor = maior = n1
# Verificando quem é MENOR
if n2 < menor:
    menor = n2
if n2 > maior:
    maior = n2
# Verificando quem é MAIOR
if n3 < menor:
    menor = n3
if n3 > maior:
    maior = n3"""

menor = min(n1, n2, n3)
maior = max(n1, n2, n3)

print(f'O menor valor digitado foi {menor}')
print(f'O menor valor digitado foi {maior}')
