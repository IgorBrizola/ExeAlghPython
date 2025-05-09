maiorNumero = 0 
menorNumero = 0 

while True:
    numero = int(input("Digite um numero: "))

    if (numero < 0):
        break
    
    if (maiorNumero == 0 and menorNumero == 0):
        maiorNumero = numero
        menorNumero = numero
    elif (numero > maiorNumero):
        maiorNumero = numero
    elif (numero < menorNumero):
        menorNumero = numero

print(f"\nO maior numero eh: {maiorNumero}")
print(f"\nO menor numero eh: {menorNumero}")

