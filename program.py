from time import sleep
import services, utils

"""
Perguntar a cidade
Pegar as coordenadas(lat e lon)
Pegar o clima
Mostrar o vento e a temperatura
"""

def display_climate():
    return 0

def display_coordenates():
    return 0

utils.clean_terminal()

city = input("Digite um nome de uma cidade que vai ser retornado o clima de tal." \
            "\n\n")

coordenates = services.get_coordenates(city)
latitude = coordenates[0]
longitude = coordenates[1]

utils.clean_terminal()
def carregando():
    quantities = 0
    while(quantities <= 2):
        print(".", end="", flush=True)
        quantities += 1
        sleep(1)
    print()
carregando()
sleep(2)

utils.clean_terminal()

print(f"As coordenadas de {city} são:")
print(f"lat: {latitude}")
print(f"lon: {longitude}")



#climate = services.get_climate(latitude, longitude)