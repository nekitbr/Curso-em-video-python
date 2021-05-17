# criar uma lista com nomes de alunos, e outra lista dentro da primeira lista com as notas desse aluno
# logo em seguida, mostrar o nome seguido da média

nomes=[]
while True:
    nomestemp=str(input('Digite o nome do aluno: '))
    notas1temp=float(input('Digite a primeira nota do aluno: '))
    notas2temp=float(input('Digite a segunda nota do aluno: '))
    media=((notas1temp+notas2temp)/2)
    nomes.append([nomestemp, [notas1temp, notas2temp], media])
    pararvar=input('deseja adicionar outro aluno?').upper().strip()
    if pararvar in 'N':
        del(pararvar, nomestemp, notas1temp, notas2temp, media)
        break
print('Os alunos cadastrados foram:')
for a, i in enumerate(nomes):
#   por algum motivo o (a) tá puxando a posição de um perfil inteiro dos alunos, deixando o (i) com
#   a posição do nome, ambas as notas e a média
    print(f'O aluno de nome {i[0]} tirou as notas {i[1]}, resultando numa média de {i[2]}')