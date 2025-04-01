ARROZ: int = 204
FEIJAO: int = 110
FRANGO: int = 165

porcao_arroz = int(input("Insira a quantidade de porções de arroz: ")) * ARROZ
porcao_feijao = int(input("Insira a quantidade de porções de feijao: ")) * FEIJAO
porcao_frango = int(input("Insira a quantidade de porções de frango: ")) * FRANGO

def calcular_calorias(kcal_arroz, kcal_feijao, kcal_frango):
    print(f"Você está ingerindo cerca de {kcal_arroz} kcal de arroz")
    print(f"Você está ingerindo cerca de {kcal_feijao} kcal de feijão")
    print(f"Você está ingerindo cerca de {kcal_frango} kcal de frango")
    print(f"Você está ingerindo um total de {kcal_arroz + kcal_feijao + kcal_frango} kcal")

calcular_calorias(porcao_arroz, porcao_feijao, porcao_frango)