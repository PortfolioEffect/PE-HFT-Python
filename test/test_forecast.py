import unittest
import configparser
from hft.util import *
from hft.plot import *
from hft.portfolio import *
from hft.position import *
from hft.forecast import *
from hft.optimization import *


class TestForecast(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        config = configparser.ConfigParser()
        config.read('credentials.ini')

        util_setCredentials(config['DEFAULT']['username'],
                            config['DEFAULT']['password'],
                            config['DEFAULT']['apiKey'])
        super(TestForecast, self).__init__(*args, **kwargs)

    def test_simple_forecast(self):
        portfolio = Portfolio('t-1', 't', 'SPY')
        positionG = portfolio.add_position('GOOG', 100)
        positionA = portfolio.add_position('AAPL', 100)
        forecast_object = Forecast(positionA.variance())
        forecast_object = forecast_object.input(positionA.beta())
        forecast_vector = compute(forecast_object.apply())

        # assert len(VariancePortfolio[0]) > 0
        assert len(forecast_vector[0]) > 0

    def test_forecast_settings_model(self):
            portfolio1 = Portfolio('2015-06-12 09:30:00', '2015-06-14 16:00:00', 'SPY')
            positionG = portfolio1.add_position('GOOG', 100)
            positionA = portfolio1.add_position('AAPL', 100)
            forecast_object = Forecast(positionA.variance())
            forecast_object = forecast_object.input( positionA.beta())
            forecast_vector1 = compute(forecast_object.apply())
            forecast_object = Forecast(positionA.variance(),model='HAR')
            forecast_object = forecast_object.input( positionA.beta())
            forecast_vector2 = compute(forecast_object.apply())

            assert not forecast_vector1[0][1][len(forecast_vector1[0][1]) - 1] - forecast_vector2[0][1][len(forecast_vector2[0][1]) - 1] == 0


    def test_forecast_settings_window(self):
     portfolio1 = Portfolio('2015-06-12 09:30:00', '2015-06-14 16:00:00', 'SPY')
     positionG = portfolio1.add_position('GOOG', 100)
     positionA = portfolio1.add_position('AAPL', 100)
     forecast_object = Forecast(positionA.variance(), window="5d")
     forecast_object = forecast_object.input( positionA.beta())
     forecast_vector1 = compute(forecast_object.apply())
     forecast_object = Forecast(positionA.variance(), window="10d")
     forecast_object = forecast_object.input( positionA.beta())
     forecast_vector2 = compute(forecast_object.apply())

     assert not forecast_vector1[0][1][len(forecast_vector1[0][1]) - 1] - forecast_vector2[0][1][len(forecast_vector2[0][1]) - 1] == 0

    def test_forecast_settings_step(self):
         portfolio1 = Portfolio('2015-06-12 09:30:00', '2015-06-14 16:00:00', 'SPY')
         positionG = portfolio1.add_position('GOOG', 100)
         positionA = portfolio1.add_position('AAPL', 100)
         forecast_object = Forecast(positionA.variance(), step = "1d")
         forecast_object = forecast_object.input( positionA.beta())
         forecast_vector1 = compute(forecast_object.apply())
         forecast_object = Forecast(positionA.variance(), step = "1h")
         forecast_object = forecast_object.input( positionA.beta())
         forecast_vector2 = compute(forecast_object.apply())

         assert not forecast_vector1[0][1][len(forecast_vector1[0][1]) - 1] - forecast_vector2[0][1][
             len(forecast_vector2[0][1]) - 1] == 0

    def test_forecast_settings_transform(self):
     portfolio1 = Portfolio('2015-06-12 09:30:00', '2015-06-14 16:00:00', 'SPY')
     positionG = portfolio1.add_position('GOOG', 100)
     positionA = portfolio1.add_position('AAPL', 100)
     forecast_object = Forecast(positionA.variance(), transform ="log")
     forecast_object = forecast_object.input( positionA.beta())
     forecast_vector1 = compute(forecast_object.apply())
     forecast_object = Forecast(positionA.variance(), transform ="none")
     forecast_object = forecast_object.input( positionA.beta())
     forecast_vector2 = compute(forecast_object.apply())

     assert not forecast_vector1[0][1][len(forecast_vector1[0][1]) - 1] - forecast_vector2[0][1][len(forecast_vector2[0][1]) - 1] == 0

    def test_forecast_settings_seasonalityInterval(self):
         portfolio1 = Portfolio('2015-06-12 09:30:00', '2015-06-14 16:00:00', 'SPY')
         positionG = portfolio1.add_position('GOOG', 100)
         positionA = portfolio1.add_position('AAPL', 100)
         forecast_object = Forecast(positionA.variance(), seasonalityInterval='none')
         forecast_object = forecast_object.input( positionA.beta())
         forecast_vector1 = compute(forecast_object.apply())
         forecast_object = Forecast(positionA.variance(), seasonalityInterval='1h')
         forecast_object = forecast_object.input( positionA.beta())
         forecast_vector2 = compute(forecast_object.apply())

         assert not forecast_vector1[0][1][len(forecast_vector1[0][1]) - 1] - forecast_vector2[0][1][
             len(forecast_vector2[0][1]) - 1] == 0

    def test_forecast_settings_updateInterval(self):
        portfolio1 = Portfolio('2015-06-12 09:30:00', '2015-06-14 16:00:00', 'SPY')
        positionG = portfolio1.add_position('GOOG', 100)
        positionA = portfolio1.add_position('AAPL', 100)
        forecast_object = Forecast(positionA.variance(), updateInterval="1m")
        forecast_object = forecast_object.input(positionA.beta())
        forecast_vector1 = compute(forecast_object.apply())
        forecast_object = Forecast(positionA.variance(), updateInterval="5m")
        forecast_object = forecast_object.input(positionA.beta())
        forecast_vector2 = compute(forecast_object.apply())

        assert not forecast_vector1[0][1][len(forecast_vector1[0][1]) - 1] - forecast_vector2[0][1][
            len(forecast_vector2[0][1]) - 1] == 0

    def test_forecast_settings_valueType(self):
     portfolio1 = Portfolio('2015-06-12 09:30:00', '2015-06-14 16:00:00', 'SPY')
     positionG = portfolio1.add_position('GOOG', 100)
     positionA = portfolio1.add_position('AAPL', 100)
     forecast_object = Forecast(positionA.variance(), valueType="forecast")
     forecast_object = forecast_object.input(positionA.beta())
     forecast_vector1 = compute(forecast_object.apply())
     forecast_object = Forecast(positionA.variance(), valueType="error")
     forecast_object = forecast_object.input(positionA.beta())
     forecast_vector2 = compute(forecast_object.apply())

     assert not forecast_vector1[0][1][len(forecast_vector1[0][1]) - 1] - forecast_vector2[0][1][len(forecast_vector2[0][1]) - 1] == 0

    def test_forecast_settings(self):
         portfolio1 = Portfolio('2015-06-12 09:30:00', '2015-06-14 16:00:00', 'SPY')
         positionG = portfolio1.add_position('GOOG', 100)
         positionA = portfolio1.add_position('AAPL', 100)
         forecast_object = Forecast(positionA.variance())
         forecast_object = forecast_object.input(positionA.beta())
         forecast_vector1 = compute(forecast_object.apply())
         forecast_object = Forecast(positionA.variance())
         forecast_vector2 = compute(forecast_object.apply())

         assert not forecast_vector1[0][1][len(forecast_vector1[0][1]) - 1] - forecast_vector2[0][1][
             len(forecast_vector2[0][1]) - 1] == 0


if __name__ == '__main__':
    unittest.main()