import requests

import openmeteo_requests #search for climate
import requests_cache
from retry_requests import retry

# Setup the Open-Meteo API client with cache and retry on error
cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
openmeteo = openmeteo_requests.Client(session = retry_session)

"""
Usar api para buscar as coordenadas e retornar a lat e lon
Buscar o clima api e retornar temperatura, elevação e precipitação
"""

#---------------------------------------------------------------------

def get_climate(lat, lon):

    url = "https://api.open-meteo.com/v1/forecast"
    params = {
    "latitude": lat,
    "longitude": lon,
    "current": ["temperature_2m", "wind_speed_10m", "precipitation"],
    "timezone": "auto",       # <-- Resolvido! A API detecta o fuso local sozinha
    }

    responses = openmeteo.weather_api(url, params = params)
    response = responses[0]
    current = response.Current()

    temp = current.Variables(0).Value()  # temperature_2m
    wind = current.Variables(1).Value()  # wind_speed_10m
    precipitation = current.Variables(2).Value()

    return {
        "temp":  round(temp, 1),
        "wind":        round(wind, 1),
        "precipitation": round(precipitation, 1)
    }

def get_coordenates(city):
    url_api = "https://geocoding-api.open-meteo.com/v1/search"
    params = {"name": city, "count": 1, "language": "pt", "format": "json"}

    try:
        response = requests.get(url_api, params=params)
        response.raise_for_status()
        data = response.json()

        if not data.get('results'):  # ✅ API found nothing
            print(f"Cidade '{city}' não encontrada.")
            return None
        
        latitude_longitude = [data['results'][0]['latitude'], data['results'][0]['longitude']]
        return latitude_longitude
    except requests.exceptions.ConnectionError:
        print("Sem conexão com a internet.")
    except requests.exceptions.Timeout:
        print("A requisição demorou demais.")
    except requests.exceptions.HTTPError as e:
        print(f"Erro HTTP: {e}")

def verify_city(city):
    url = "https://nominatim.openstreetmap.org/search"
    params = {"q": city, "format": "json", "limit": 1}
    headers = {"User-Agent": "ClimateConsulter/1.0"}

    try:
        response = requests.get(url, params=params, headers=headers, timeout=5)
        response.raise_for_status()
        data = response.json()

        if data:
            return True
        else:
            print("Cidade não encontrada.")
            return False
    except requests.exceptions.ConnectionError:
        print("Sem conexão.")
        return False
    except requests.exceptions.Timeout:
        print("Requisição demorou demais.")
        return False