import random
aluno1 = input('Primeiro aluno: ')
aluno2 = input('Segundo aluno: ')
aluno3 = input('Terceiro aluno: ')
aluno4 = input('Quarto aluno: ')
lista_alunos = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(lista_alunos)
print(f'A ordem de apresentação do trabalho será')
print(lista_alunos)