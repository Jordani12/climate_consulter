import requests

import openmeteo_requests
import requests_cache
from retry_requests import retry

# Setup the Open-Meteo API client with cache and retry on error
cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
openmeteo = openmeteo_requests.Client(session = retry_session)

"""
Usar api para buscar as coordenadas e retornar a lat e lon
Buscar o clima com a mesma api
"""

#---------------------------------------------------------------------

def get_climate(lat, lon):

    url = "https://api.open-meteo.com/v1/forecast"
    params = {
    "latitude": lat,
    "longitude": lon,
    "hourly": "temperature_2m",
    "timezone": "auto",       # <-- Resolvido! A API detecta o fuso local sozinha
    "forecast_days": 1,
    }

    responses = openmeteo.weather_api(url, params = params)
    response = responses[0]
    type_responses = [response.Elevation(), response.Timezone(), response.TimezoneAbbreviation(), response.UtcOffsetSeconds()]

    return type_responses

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
