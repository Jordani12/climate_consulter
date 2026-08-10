import requests

"""
Usar api para buscar as coordenadas e retornar a lat e lon
Buscar o clima com a mesma api
"""


def get_climate(lat, lon):
    return 0


def get_coordenates(city):
    url_api = "https://geocoding-api.open-meteo.com/v1/search"
    params = {"name": city, "count": 1, "language": "pt", "format": "json"}

    try:
        response = requests.get(url_api, params=params)
        response.raise_for_status()
        data = response.json()
        latitude_longitude = [data['results'][0]['latitude'], data['results'][0]['longitude']]
        return latitude_longitude
    except requests.exceptions.ConnectionError:
        print("Sem conexão com a internet.")
    except requests.exceptions.Timeout:
        print("A requisição demorou demais.")
    except requests.exceptions.HTTPError as e:
        print(f"Erro HTTP: {e}")
