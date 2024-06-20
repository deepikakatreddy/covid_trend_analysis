import pandas as pd

def preprocess_covid_data(covid_data, country):
    columns_of_interest = ['date', 'total_cases', 'new_cases', 'total_deaths', 'new_deaths', 'total_vaccinations']
    country_data = covid_data[covid_data['location'] == country][columns_of_interest].dropna()
    country_data['date'] = pd.to_datetime(country_data['date'])
    country_data['daily_new_cases'] = country_data['new_cases'].diff()
    country_data['daily_new_deaths'] = country_data['new_deaths'].diff()
    return country_data
