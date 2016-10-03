import unittest
import configparser
from hft.util import *
from hft.plot import *
from hft.portfolio import *
from hft.position import *
from hft.metric import *


class TestGreatePortfolio(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        config = configparser.ConfigParser()
        config.read('credentials.ini')

        util_setCredentials(config['DEFAULT']['username'],
                            config['DEFAULT']['password'],
                            config['DEFAULT']['apiKey'],
                            config['DEFAULT']['host'])
        super(TestGreatePortfolio, self).__init__(*args, **kwargs)

    def test_simpleCreate(self):
        portfolio = Portfolio('t-1', 't', 'SPY')
        positionG = portfolio.add_position('GOOG', 100)
        positionA = portfolio.add_position('AAPL', 100)
        Variance = compute(portfolio.variance())
        assert len(Variance[0][0]) > 0

    def test_simpleCreateTime(self):
        portfolio = Portfolio("2014-09-01 09:00:00", "2014-09-14 16:00:00")
        positionG = portfolio.add_position('GOOG', 100)
        positionA = portfolio.add_position('AAPL', 100)
        Variance = compute(portfolio.variance())
        portfolio
        assert len(Variance[0][0]) > 0



    def test_createWithData(self):
        portfolio = Portfolio('t-3', 't', 'SPY')
        positionG = portfolio.add_position('GOOG', 100)
        positionA = portfolio.add_position('AAPL', 100)
        priceG = compute(positionG.price())[0]
        portfolio = Portfolio(indexData=priceG)
        positionA = portfolio.add_position('AAPL', quantity=100)
        Variance = compute(portfolio.value())
        # portfolio.value().plot()
        assert len(Variance[0][0]) > 0


if __name__ == '__main__':
    unittest.main()
