import unittest
import configparser
from hft.util import *
from hft.plot import *
from hft.portfolio import *

class TestPositionMetrics(unittest.TestCase):
    
    def __init__(self, *args, **kwargs):
        config = configparser.ConfigParser()
        config.read('credentials.ini')
        
        util_setCredentials(config['DEFAULT']['username'], 
                            config['DEFAULT']['password'], 
                            config['DEFAULT']['apiKey'], 
                            config['DEFAULT']['host'])
        
        super(TestPositionMetrics, self).__init__(*args, **kwargs)
    
    def setUp(self): 
        self.portfolio = portfolio_create('t-1', 't', 'SPY')
        self.symbol = 'GOOG'
        portfolio_addPosition(self.portfolio, self.symbol, 100)

        
    def test_position_varince(self):
        value = position_variance(self.portfolio, self.symbol)
        assert len(value[0]) > 0
        
    def test_position_kurtosis(self):
        value = position_kurtosis(self.portfolio, self.symbol)
        assert len(value[0]) > 0
        
    def test_position_skewness(self):
        value = position_skewness(self.portfolio, self.symbol)
        assert len(value[0]) > 0
        
    def test_position_hurstExponent(self):
        value = position_hurstExponent(self.portfolio, self.symbol)
        assert len(value[0]) > 0
    
    def test_position_fractalDimension(self):
        value = position_fractalDimension(self.portfolio, self.symbol)
        assert len(value[0]) > 0        
        #util_plot2d(variance, "GOOG Variance", "daily")

if __name__ == '__main__':
    unittest.main()