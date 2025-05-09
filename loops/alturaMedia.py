

quantidadeHomem = 0
quantidadeMulher = 0

alturaTotalHomem = 0
alturaTotalMulher = 0

alturaMediaMulher = 0
alturaMediaHomem = 0

contadora = 0

totalDePessoas = int(input("Digite o total de pessoas que deseja cadastrar: "))

def validaGenero(genero, altura):
    global quantidadeHomem, quantidadeMulher
    global alturaTotalHomem, alturaTotalMulher
    global alturaMediaHomem, alturaMediaMulher
 
    if (genero == "m"):
        quantidadeHomem += 1
        if (altura < 0 ): return "altura invaldia!"
        alturaTotalHomem += altura
        alturaMediaHomem = alturaTotalHomem / quantidadeHomem
    elif (genero == "f"):
         quantidadeMulher += 1
         if (altura < 0 ): return "altura invaldia!"
         alturaTotalMulher += altura
         alturaMediaMulher = alturaTotalMulher / quantidadeMulher
    else:
        return "genero invalido!"


def identificaPessoa():
    genero = str(input("Digite seu genero, M para masculino e F para feminino: ")).lower()
    altura = float(input("Digite sua altura: "))

    validaGenero(genero, altura)
    


while (contadora < totalDePessoas):
    pessoa = identificaPessoa()
    
    contadora += 1


print(f"Total de homens: {quantidadeHomem}")
print(f"Total de mulheres: {quantidadeMulher}")


print(f"Altura media dos homens: {alturaMediaHomem}")
print(f"Altura media das mulheres: {alturaMediaMulher}")