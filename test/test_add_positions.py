import unittest
import configparser
from hft.util import *
from hft.plot import *
from hft.portfolio import *
from hft.position import *
from hft.metric import *

class TestAddpositionMethods(unittest.TestCase):
         
    def __init__(self, *args, **kwargs):
        config = configparser.ConfigParser()
        config.read('credentials.ini')
        
        util_setCredentials(config['DEFAULT']['username'], 
                            config['DEFAULT']['password'], 
                            config['DEFAULT']['apiKey'], 
                            config['DEFAULT']['host'])
        super(TestAddpositionMethods, self).__init__(*args, **kwargs)
        
    def test_addSingleQuantity(self):
        portfolio = Portfolio('t-1', 't', 'SPY')
        positionG = portfolio.add_position('GOOG', 100)
        positionA = portfolio.add_position('AAPL', 100)
        Variance = compute(portfolio.variance())
        assert   len(Variance[0][0])>0


    def test_addMultipleQuantities(self):
       portfolio = Portfolio('2015-06-12 09:30:00', '2015-06-14 16:00:00', 'SPY')
       position =portfolio.add_position('AAPL', [100, 200], [1434117340000, 1434290140000])
       Variance = compute(portfolio.variance())
       assert len(Variance[0][0])>0

    def test_addMultipleQuantities(self):
       portfolio = Portfolio('2015-06-12 09:30:00', '2015-06-20 16:00:00', 'SPY')
       position =portfolio.add_position('AAPL', [100, 200], ['2015-06-12 09:55:00', '2015-06-16 09:55:00'])
       Variance = compute(portfolio.variance())
       # position.quantity().plot()
       assert len(Variance[0][0])>0

    def test_addSingleQuantityFromData(self):
        portfolio = Portfolio('t-3', 't', 'SPY')
        positionG = portfolio.add_position('GOOG', 100)
        positionA = portfolio.add_position('AAPL', 100)
        price = compute(positionA.price())

        portfolio = Portfolio('t-3', 't', 'SPY')
        positionA = portfolio.add_position('AAPL',quantity=100, priceData=price[0])
        print positionA
        Variance = compute(portfolio.variance())
        assert len(Variance[0][0]) > 0
 
if __name__ == '__main__':
    unittest.main()
