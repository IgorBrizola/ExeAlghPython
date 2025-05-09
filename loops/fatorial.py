fatorial = 1


numero = int(input("Digite um numero: "))


def validarNumero(numero):
    if (numero < 0):
        return "não é possivel calcular o fatorial de numeros menores que zero!"

validarNumero(numero)

for i in range(1, numero + 1):
    fatorial *= i


