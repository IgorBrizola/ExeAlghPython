print('---------------------------------------------------')

valor_gasto = float(input('Digite o valor total consumido: R$'))

porcentagem_garcom = float(input('\nDigite a porcentagem de comissão para o garçom: %'))

def taxa_garcom(valor_gasto, porcentagem_garcom):
    return valor_gasto * (porcentagem_garcom / 100)

def total_pagar(taxa_garcom):
    return valor_gasto + taxa_garcom

print(f'\nO valor total a ser pago considerando %{porcentagem_garcom} do garçom é de: R${total_pagar(taxa_garcom(valor_gasto, porcentagem_garcom))}\n')

print('---------------------------------------------------')