salario = float(input('Qual é o salário do funcionário? R$'))
aumento = salario * 15 / 100
salario_final = salario + aumento
print(f'Um funcionário que ganhava R${salario:.2f}, com 15% de aumento passa a ganhar R${salario_final:.2f}')