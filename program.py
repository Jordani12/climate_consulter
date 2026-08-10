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

def wait_to_load():
    utils.clean_terminal()
    utils.loading()
    sleep(2)
    utils.clean_terminal()

def display_climate(latitude, longitude):
    wait_to_load()
    get_climate = services.get_climate(latitude, longitude)

    temp = get_climate['temp']
    wind_speed = get_climate['wind'] 
    precipitation = get_climate['precipitation']

    print(f"Temp is: {temp}°C")
    print(f"Wind speed is: {wind_speed}")
    print(f"And the precipitation is: {precipitation}mm")

def display_coordenates(city):
    wait_to_load()
    coordenates = services.get_coordenates(city)
    latitude = coordenates[0]
    longitude = coordenates[1]
    
    print(f"The {city} coordinates is:")
    print(f"lat: {latitude}")
    print(f"lon: {longitude}")

    return latitude, longitude

#---------------------------------------------------------------------

while(True):
    city = input("Type one real city and it'll return the climate." \
                "\n\n")

    lat_lon = display_coordenates(city)

    sleep(3)
    display_climate(lat_lon[0], lat_lon[1])

    input("Press enter to return.")