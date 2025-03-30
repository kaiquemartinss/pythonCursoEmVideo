num = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para conversão: ')
print('[1] converter para BINÁRIO')
print('[2] converter para OCTAL')
print('[3] converter para HEXADECIMAL')
opt = int(input('Sua opção: '))

if opt == 1:
    binario = bin(num)
    print(f'{num} convertido para BINÁRIO é igual a {binario[2:]}')
elif opt == 2:
    octal = oct(num)
    print(f'{num} convertido para OCTAL é igual a {octal[2:]}')
elif opt == 3:
    hexadecimal = hex(num)
    print(f'{num} convertido para HEXADECIMAL é igual a {hexadecimal[2:]}')
else:
    print('OPÇÃO INVÁLIDA!')