fatorial = 1

numero = int(input("Digite um numero: "))

def calcFatorial(numero):
    global fatorial
    if (numero < 0):
        return "não é possivel calcular o fatorial de numeros negativos!"
    else:
        for i in range(1, numero + 1):
         fatorial *= i
        return f"O fatorial do numero {numero} eh = {fatorial}"

print(calcFatorial(numero))
