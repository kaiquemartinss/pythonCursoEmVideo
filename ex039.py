from datetime import datetime
sexo = input('Qual o seu sexo? [M/F]: ')

if sexo == 'F':
    print('Você não precisa realizar o alistamento militar')
else:
    nasc = int(input('Ano de nascimento: '))
    ano_atual = datetime.now().year
    idade = ano_atual - nasc
    
    print(f'Quem nasceu em {nasc} tem {idade} anos em {ano_atual}')
    if idade < 18:
        diferenca_idade =  18 - idade
        ano_alistamento = ano_atual + diferenca_idade
        print(f'Ainda faltam {diferenca_idade} para o alistamento.')
        print(f'Seu alistamento será em {ano_alistamento}.')
    elif idade > 18:
        diferenca_idade = idade - 18
        ano_alistamento = ano_atual - diferenca_idade
        print(f'Você já deveria ter se alistado a {diferenca_idade} anos.')
        print(f'Seu alistamento foi em {ano_alistamento}.')
    else:
        print('Você tem que se alistar IMEDIATAMENTE!')