print('---------------------------------------------------')

distancia = int(input('\nDigite a distancia: '))

tempo = int(input('\nDigite o tempo em horas: '))

def calc_km(distancia, tempo):
    return distancia / tempo

print(f"\nA velocidade media da viagem será de {calc_km(distancia, tempo)} km/h")

print('---------------------------------------------------')