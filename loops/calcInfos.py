

idades = [18, 30, 51, 34, 17, 12, 14, 19, 13, 10,
          12, 19, 15, 14, 14, 12, 10, 60, 70, 99,
          12, 8, 7, 16, 45, 20, 21, 25, 28, 32]

alturas = [1.78, 2.00, 1.65, 1.78, 1.78, 1.35, 1.56, 1.78, 1.66, 1.45,
           1.68, 1.75, 1.55, 1.45, 1.45, 1.33, 1.32, 1.55, 1.56, 1.43,
           1.45, 1.00, 1.00, 1.40, 1.67, 1.50, 1.60, 1.72, 1.70, 1.68]

pesos = [80.00, 90.00, 72.34, 60.00, 70.00, 20.00, 34.00, 60.00, 30.00, 20.00,
         20.00, 70.00, 80.00, 90.00, 35.00, 25.00, 23.00, 56.00, 48.00, 30.00,
         30.00, 20.00, 20.00, 40.00, 60.00, 55.00, 62.00, 75.00, 68.00, 66.00]

def registraPessoas():
    for i in range(1, 11):
        print(f"\nPESSOA - {i}")
        idade = int(input("Digite sua idade: "))
        altura = float(input("Digite sua altura: "))
        peso = float(input("Digite seu peso: "))

        idades.append(idade)
        alturas.append(altura)
        pesos.append(peso)

def calcIdade():
    pessoas50mais = 0

    for x in idades:
        if x > 50:
            pessoas50mais += 1
    
    return pessoas50mais

def calcMediaAltura():
    quantidadeAltura = 0
    somaAlturas = 0
   
    for idade, altura in zip (idades, alturas):
        if idade >= 10 and idade <= 20:
            quantidadeAltura += 1
            somaAlturas += altura
    
    media_altura = somaAlturas / quantidadeAltura

    return round(media_altura, 2)
    
def calcPesoAbaixo():
    global pesos

    quantidadePessoas = 0

    for i in pesos:
        if i < 40.00:
            quantidadePessoas += 1

    return round(((quantidadePessoas / len(pesos)) * 100), 2)

# registraPessoas()

print(f"\nA quantidade de pessoas com idade superior a 50 anos = {calcIdade()}")
print(f"\nA média das alturas das pessoas com idade entre 10 e 20 anos = {calcMediaAltura()}m")
print(f"\nA porcentagem de pessoas com peso inferior a 40 quilos entre todas as pessoas analisadas = {calcPesoAbaixo()}%")


    
    
    

    