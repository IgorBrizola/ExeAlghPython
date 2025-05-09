
soma_pares = 0

def calcula_par(numero):
    global soma_pares
    if (numero % 2 == 0):
        soma_pares += numero

for i in range(20, 400 + 1):
    calcula_par(i)


print(f"a soma dos numeros pares de 20 a 400 = {soma_pares}")

 
    




