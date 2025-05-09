numerosPositivos = 0
numerosNegativos = 0

maiorNumero = 0 
menorNumero = 0 

   
while True:
    numero = int(input("Digite um numero: "))

    if (numero == 0):
        break

    if (numero > 0):
        if (numero > maiorNumero):
            maiorNumero = numero
        numerosPositivos += 1
    else:
        if (numero < menorNumero):
            menorNumero = numero
        numerosNegativos += 1


    
print(f"\nA quantidade de números positivos eh: {numerosPositivos}")
print(f"\nA quantidade de números negativos eh: {numerosNegativos}")

print(f"\nO maior numero eh: {maiorNumero}")
print(f"\nO menor numero eh: {menorNumero}")
