import unittest
import configparser
from hft.util import *
from hft.plot import *
from hft.portfolio import *

class TestAddPositionMethods(unittest.TestCase):
        
    def __init__(self, *args, **kwargs):
        config = configparser.ConfigParser()
        config.read('credentials.ini')
        
        util_setCredentials(config['DEFAULT']['username'], 
                            config['DEFAULT']['password'], 
                            config['DEFAULT']['apiKey'], 
                            config['DEFAULT']['host'])
        super(TestAddPositionMethods, self).__init__(*args, **kwargs)
        
    def test_addSingleQuantity(self):
        portfolio = portfolio_create('t-1', 't', 'SPY')
        portfolio_addPosition(portfolio, 'GOOG', 100)
        variance = position_variance(portfolio, 'GOOG')
        assert len(variance[0]) > 0
     
        
    def test_addMultipleQuantities(self):
        portfolio = portfolio_create('2015-06-12 09:30:00', '2015-06-14 16:00:00', 'SPY')
        portfolio_addPosition(portfolio, 'AAPL', [100, 200], ["2015-06-12 09:55:40", "2015-06-14 09:55:40"])
        variance = position_variance(portfolio, 'AAPL')
        assert len(variance[0]) > 0    
        #util_plot2d(variance, "GOOG Variance", "daily")


 
if __name__ == '__main__':
    unittest.main()