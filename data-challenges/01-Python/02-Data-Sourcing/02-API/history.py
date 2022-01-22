# pylint: disable=missing-docstring

import sys
import requests

from weather import search_city


def daily_forecast(woeid, year, month, day):
    url = f"https://www.metaweather.com/api/location/{woeid}/{year}/{month}/{day}/"
    response = requests.get(url).json()
    return response


def monthly_forecast(woeid, year, month):
    """ return a `list` of forecasts for the whole month """
    forecasts = []
    for i in range(1, 29):
        for x in daily_forecast(woeid, year, month, i):
            forecasts.append(x)
        print(forecasts)
    return forecasts


def write_csv(woeid, year, month, city, forecasts):
    """ dump all the forecasts to a CSV file in the `data` folder """
    return None

def main():
    if len(sys.argv) > 2:
        city = search_city(sys.argv[1])
        if city:
            woeid = city['woeid']
            year = int(sys.argv[2])
            month = int(sys.argv[3])
            if 1 <= month <= 12:
                forecasts = monthly_forecast(woeid, year, month)
                if not forecasts:
                    print("Sorry, could not fetch any forecast")
                else:
                    write_csv(woeid, year, month, city['title'], forecasts)
            else:
                print("MONTH must be a number between 1 (Jan) and 12 (Dec)")
                sys.exit(1)
    else:
        print("Usage: python history.py CITY YEAR MONTH")
        sys.exit(1)


if __name__ == '__main__':
    main()
