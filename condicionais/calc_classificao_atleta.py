
CATEGORIA_INFANTIL_A = "Infantil A"
CATEGORIA_INFANTIL_B = "Infantil B"

CATEGORIA_JUVENIL_A = "Juvenil A"
CATEGORIA_JUVENIL_B = "Juvenil B"

CATEGORIA_ADULTO = "Adulto"


nome = str(input("Digite seu nome: "))
idade = int(input("Digite sua idade: "))

def classificar_atleta(idade):
    if (idade >= 0 and idade <= 7): 
        return CATEGORIA_INFANTIL_A
    elif(idade >= 8 and idade <= 10):
        return CATEGORIA_INFANTIL_B
    elif(idade >= 11 and idade <= 13):
        return CATEGORIA_JUVENIL_A
    elif(idade >= 14 and idade <= 17):
        return CATEGORIA_JUVENIL_B
    elif(idade >= 18 and idade <= 59): 
        return CATEGORIA_ADULTO
    elif(idade >= 60):
        return CATEGORIA_ADULTO
    else: return print("Idade invalida!")
    
def calc_taxa():
    classificacao = classificar_atleta(idade)
    if (classificacao == "Infantil A"):
        return 50.00 
    elif(classificacao == "Infantil B"):
        return 70.00
    elif(classificacao == "Juvenil A"):
        return 100.00
    elif(classificacao == "Juvenil B"):
        return 130.00
    elif(classificacao == "Adulto"):
        return 180.00 
    else: return print("Classificação invalida!")

def calc_desconto(idade):
    if (idade <= 17):
        return 10
    elif(idade >= 18 and idade <= 59):
            return 0
    elif(idade >= 60):
            return 30
    else: return print("Desconto não aplicavel!")

def calc_valor_final(idade):
    taxa = calc_taxa()
    desconto = calc_desconto(idade)
    if (desconto != 0 ): return (taxa - (taxa * (desconto / 100))) 
    else: return taxa
     

classificacao = classificar_atleta(idade)
taxa = calc_taxa()
desconto = calc_desconto(idade)
valor_final = calc_valor_final(idade)

print(f"Altleta: {nome} \nCategoria: {classificacao} \nTaxa original: R${taxa} \nDeconto aplicado: {desconto}%  \nValor Final: R${valor_final}")