dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
preco_dia = 60
km_rodado = 0.15
total = preco_dia * dias + km_rodado * km
print(f'O valor total a pagar é de R${total:.2f}')