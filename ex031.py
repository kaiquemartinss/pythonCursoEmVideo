distancia = float(input('Qual é a distância da sua viagem?'))
print(f'Você está prestes a começar uma viagem de {distancia}Km.')
preco = 0
if distancia <= 200:
    preco = distancia * 0.5
else:
    preco = distancia * 0.45
print(f'E o preço da sua passagem será de R${preco:.2f}')
