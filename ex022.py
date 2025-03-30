nome = input('Digite seu nome completo: ').strip()
print('Analisando seu nome...')
quantidade = len(nome.replace(" ", ""))
primeiro_nome = nome.split()[0]
quantidade_primeiro_nome = len(primeiro_nome)
print(f'Seu nome em maiúsculas é {nome.upper()}')
print(f'Seu nome em minúsculas é {nome.lower()}')
print(f'Seu nome tem ao todo {quantidade} letras')
print(f'Seu primeiro nome é {primeiro_nome} e ele tem {quantidade_primeiro_nome} letras')