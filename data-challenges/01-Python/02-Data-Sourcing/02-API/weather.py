# pylint: disable=missing-module-docstring

import sys
import requests

BASE_URI = "https://www.metaweather.com"


def search_city(query):
    '''Look for a given city and disambiguate between several candidates.
    Return one city (or None)'''
    url = f"https://www.metaweather.com/api/location/search/?query={query}"
    response = requests.get(url).json()
    if len(response) == 1:
        out = response[0]
    elif len(response) > 1:
        for i, v in enumerate(response):
            print(f"{i + 1} : {v['title']}")
        choice = int(input("Which number?\n"))
        out = response[choice - 1]
    else:
        print("Can't find this city.")
        out = None
    return out


def weather_forecast(woeid):
    '''Return a 5-element list of weather forecast for a given woeid'''
    url = f"https://www.metaweather.com/api/location/{woeid}"
    response = requests.get(url).json()
    return response['consolidated_weather'][0:5]

def main():
    '''Ask user for a city and display weather forecast'''
    query = input("City?\n> ")
    city = search_city(query)
    if city:
        forecasts = weather_forecast(city['woeid'])
        for forecast in forecasts:
            print(f"{forecast['applicable_date']}: \
                {forecast['weather_state_name']} \
                    {round(forecast['the_temp'], 1)}")

if __name__ == '__main__':
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print('\nGoodbye!')
        sys.exit(0)
