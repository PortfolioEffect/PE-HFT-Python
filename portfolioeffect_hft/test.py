from portfolio import *
from plot import *
from util import *


# sample script    
util_setCredentials('username', 'password', 'api_key', 
                    'snowfall04.snowfallsystems.com')

portfolio = portfolio_create('t-1', 't', 'SPY')
portfolio_addPosition(portfolio, 'GOOG', 100)
variance = position_variance(portfolio, 'GOOG')
util_plot2d(variance, "GOOG Variance", "daily")