
soma_harmonica = 1

numero = int(input("Digite um numero: "))

def calc_harmonia(i):
    global soma_harmonica
    soma_harmonica += 1 / i

for i in range(2, numero + 1):
    calc_harmonia(i)



print(soma_harmonica)