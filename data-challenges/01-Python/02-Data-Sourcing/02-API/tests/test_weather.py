import datetime
import unittest
import weather


class TestWeather(unittest.TestCase):
    def test_search_city_for_paris(self):
        city = weather.search_city('Paris')
        self.assertEqual(city['title'], 'Paris')
        self.assertEqual(city['woeid'], 615702)

    def test_search_city_for_london(self):
        city = weather.search_city('London')
        self.assertEqual(city['title'], 'London')
        self.assertEqual(city['woeid'], 44418)

    def test_search_city_for_unknown_city(self):
        city = weather.search_city('Rouen')
        self.assertEqual(city, None)

    def test_search_city_ambiguous_city(self):
        weather.input = lambda _: "1"
        city = weather.search_city('San')
        self.assertEqual(city['title'], 'San Francisco')

    def test_weather_forecast(self):
        forecast = weather.weather_forecast(44418)
        self.assertIsInstance(forecast, list, "Did you select the `consolidated_weather` key?")
        self.assertTrue(forecast[0].get('applicable_date'))
