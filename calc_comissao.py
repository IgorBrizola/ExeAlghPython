print('---------------------------------------------------')

salario = int(input('\nDigite seu salario: R$'))

comissao = int(input('\nDigite a porcentagem de comissao: %'))

def calc_comissao(salario):
     return salario + (salario * (comissao / 100))      
    
print(f"\nSalário acrescido com a comissão de %{comissao} = {calc_comissao(salario)}")

print('---------------------------------------------------')