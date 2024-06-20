import requests
import pandas as pd

def fetch_covid_data():
    url = 'https://covid.ourworldindata.org/data/owid-covid-data.csv'
    df = pd.read_csv(url)
    return df

def fetch_additional_data():
    # Example: Fetching demographic data
    demographic_url = 'https://example.com/api/demographics'
    demographic_data = requests.get(demographic_url).json()

    # Example: Fetching healthcare capacity data
    healthcare_url = 'https://example.com/api/healthcare'
    healthcare_data = requests.get(healthcare_url).json()

    return demographic_data, healthcare_data
