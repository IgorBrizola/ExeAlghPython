print('---------------------------------------------------')
cotacao_dolar = float(input('\nDigite a cotação atual do dolar: $'))

dolar = float(input('\nDigite o valor que deseja converter para reais: $'))

def conversor(cotacao_dolar, dolar):
    return cotacao_dolar * dolar


print(f'\nO valor em reais será de R${conversor(cotacao_dolar, dolar)}\n')

print('---------------------------------------------------')