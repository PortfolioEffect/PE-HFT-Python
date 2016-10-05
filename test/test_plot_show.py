import unittest
import configparser
from hft.util import *
from hft.plot import *
from hft.portfolio import *
from hft.position import *
from hft.metric import *


class TestPlotShow(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        config = configparser.ConfigParser()
        config.read('credentials.ini')

        util_setCredentials(config['DEFAULT']['username'],
                            config['DEFAULT']['password'],
                            config['DEFAULT']['apiKey'])
        super(TestPlotShow, self).__init__(*args, **kwargs)

    def test_show(self):
        portfolio = Portfolio('t-3', 't', 'SPY')
        positionG = portfolio.add_position('GOOG', 100)
        positionA = portfolio.add_position('AAPL', 100)
        print portfolio
        print positionA
        assert 1 > 0

    def test_plot(self):
        portfolio = Portfolio("2014-09-01 09:00:00", "2014-09-04 16:00:00")
        positionG = portfolio.add_position('GOOG', 100)
        positionA = portfolio.add_position('AAPL', 100)
        portfolio.plot()
        positionA.plot()
        util_plot(portfolio.variance(),positionA.variance(),title='Variance',subtitle='variance',legend=["Portfolio","Position"])
        assert 1 > 0


if __name__ == '__main__':
    unittest.main()
