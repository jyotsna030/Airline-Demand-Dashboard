import requests
import pandas as pd

API_KEY = "cae8e7e2d01febac5174e29b0c061270"  # Replace with your AviationStack API Key
BASE_URL = "http://api.aviationstack.com/v1/flights"

def fetch_flight_data(dep_iata='SYD', limit=100):
    params = {
        'access_key': API_KEY,
        'dep_iata': dep_iata,
        'limit': limit
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return pd.DataFrame(response.json()['data'])
    else:
        raise Exception("API fetch failed.")

def clean_data(df):
    cleaned = pd.DataFrame({
        'Airline': df['airline'].apply(lambda x: x.get('name') if x else None),
        'Flight Number': df['flight'].apply(lambda x: x.get('iata') if x else None),
        'Departure Airport': df['departure'].apply(lambda x: x.get('airport') if x else None),
        'Arrival Airport': df['arrival'].apply(lambda x: x.get('airport') if x else None),
        'Departure Time': df['departure'].apply(lambda x: x.get('scheduled') if x else None),
        'Arrival Time': df['arrival'].apply(lambda x: x.get('scheduled') if x else None),
    })
    return cleaned
