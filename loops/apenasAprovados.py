alunos = ["Ana", "Bruno", "Carla", "Diego", "Eva", "Felipe"]
notas = [5.5, 8.0, 6.9, 7.1, 9.5, 4.0]

aprovados = []


for nome, nota in zip (alunos, notas):

    if (nota >= 7):
        aprovados.append(nome)


print(aprovados)