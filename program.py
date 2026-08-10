from time import sleep
import services, utils

"""
Perguntar a cidade
Pegar as coordenadas(lat e lon)
Pegar o clima
Mostrar o vento e a temperatura
"""

utils.clean_terminal()

#---------------------------------------------------------------------

def carregando():
    quantities = 0
    while(quantities <= 2):
        print(".", end="", flush=True)
        quantities += 1
        sleep(1)
    print()

def display_climate(latitude, longitude):
    utils.clean_terminal()

    carregando()

    sleep(2)

    utils.clean_terminal()

    get_climate = services.get_climate(latitude, longitude)

    elevation = get_climate[0]
    timezone = get_climate[1]
    timezone_abbreviation = get_climate[2]
    utc_offset_seconds = get_climate[3]

    print(f"Elevation: {elevation} m asl")
    print(f"Timezone: {timezone}{timezone_abbreviation}")
    print(f"Timezone difference to GMT+0: {utc_offset_seconds}s")

def display_coordenates(city):
    carregando()

    sleep(2)

    utils.clean_terminal()

    coordenates = services.get_coordenates(city)
    latitude = coordenates[0]
    longitude = coordenates[1]
    
    print(f"The {city} coordinates is:")
    print(f"lat: {latitude}")
    print(f"lon: {longitude}")

    return latitude, longitude

#---------------------------------------------------------------------

city = input("Type one real city and it'll return the climate." \
            "\n\n")

lat_lon = display_coordenates(city)

sleep(3)
display_climate(lat_lon[0], lat_lon[1])



