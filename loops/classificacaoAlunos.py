alunos = ["Ana", "Bruno", "Carla", "Diego", "Eva", "Felipe"]
notas = [5.5, 8.0, 6.9, 7.1, 9.5, 4.0]


for nome, nota in zip(alunos, notas):

    if (nota >= 7):
        print(f"{nome} foi aprovado(a)!")
    else:
        print(f"{nome} foi reprovado(a)!")



