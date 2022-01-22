import unittest
from history import daily_forecast, monthly_forecast

class TestHistory(unittest.TestCase):
    def test_daily_forecast_london_for_january_first_2019(self):
        forecast = daily_forecast(44418, 2019, 1, 1)
        self.assertEqual(len(forecast), 71)

    def test_daily_forecast_paris_for_christmas_2015(self):
        forecast = daily_forecast(615702, 2015, 12, 25)
        self.assertEqual(len(forecast), 72)

    def test_monthly_forecast_london_for_february_2019(self):
        forecasts = monthly_forecast(44418, 2019, 2)
        self.assertIsInstance(forecasts[0], dict, "Did you correctly concatenate daily forecast lists?")
        self.assertEqual(len(forecasts), 1995)

