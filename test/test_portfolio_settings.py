import unittest
import configparser
from hft.util import *
from hft.plot import *
from hft.portfolio import *

class TestSettingsMethods(unittest.TestCase):
        
    def __init__(self, *args, **kwargs):
        config = configparser.ConfigParser()
        config.read('credentials.ini')
        
        util_setCredentials(config['DEFAULT']['username'], 
                            config['DEFAULT']['password'], 
                            config['DEFAULT']['apiKey'], 
                            config['DEFAULT']['host'])
        super(TestSettingsMethods, self).__init__(*args, **kwargs)
        
    def test_updateSettings(self):
        portfolio = portfolio_create('t-1', 't', 'SPY')
        portfolio_addPosition(portfolio, 'GOOG', 100)
        portfolio_settings(portfolio, windowLength="1s")
        variance = position_variance(portfolio, 'GOOG')
        assert len(variance[0]) > 0
     
 
if __name__ == '__main__':
    unittest.main()