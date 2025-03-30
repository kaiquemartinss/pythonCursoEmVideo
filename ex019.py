import random
aluno1 = input('Primeiro aluno: ')
aluno2 = input('Segundo aluno: ')
aluno3 = input('Terceiro aluno: ')
aluno4 = input('Quarto aluno: ')
lista_alunos = [aluno1, aluno2, aluno3, aluno4]
sorteado = random.choice(lista_alunos)
print(f'O aluno escolhido foi {sorteado}')