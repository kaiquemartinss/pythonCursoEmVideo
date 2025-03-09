preco = float(input('Qual o preço do produto? R$'))
desconto = preco * 5 / 100
preco_final = preco - desconto
print(f'O produto custava R${preco:.2f}, na promoção desconto de 5% vai custar R${preco_final:.2f}')