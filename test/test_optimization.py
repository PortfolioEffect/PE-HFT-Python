import unittest
import configparser
from hft.util import *
from hft.plot import *
from hft.portfolio import *
from hft.position import *
from hft.metric import *
from hft.optimization import *


class TestOptimization(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        config = configparser.ConfigParser()
        config.read('credentials.ini')

        util_setCredentials(config['DEFAULT']['username'],
                            config['DEFAULT']['password'],
                            config['DEFAULT']['apiKey'])
        super(TestOptimization, self).__init__(*args, **kwargs)

    def test_simple_optimization(self):
        portfolio = Portfolio('t-1', 't', 'SPY')
        position = portfolio.add_position('GOOG', 100)
        position = portfolio.add_position('AAPL', 100)
        portfolio.settings( portfolioMetricsMode="price", resultsSamplingInterval='1m')
        optimizer = Optimizer(portfolio.variance(), direction="min")
        optim_portfolio = optimizer.run()
        variance_portfolio=compute(optim_portfolio.variance())
        assert len(variance_portfolio[0][0]) > 0

    def test_portfolio_optimization(self):
        portfolio = Portfolio('t-1', 't', 'SPY')
        position = portfolio.add_position('GOOG', 100)
        position = portfolio.add_position('AAPL', 100)
        portfolio.settings( portfolioMetricsMode="portfolio", resultsSamplingInterval='1m')
        optimizer = Optimizer(portfolio.variance(), direction="min")
        optim_portfolio = optimizer.run()
        variance_portfolio=compute(optim_portfolio.variance())
        assert len(variance_portfolio[0][0]) > 0

    def test_optimization_constraint(self):
            portfolio = Portfolio('t-1', 't', 'SPY')
            position = portfolio.add_position('GOOG', 100)
            position = portfolio.add_position('AAPL', 100)
            portfolio.settings( portfolioMetricsMode="price", resultsSamplingInterval='1m')
            optimizer = Optimizer(portfolio.variance(), direction="min")
            optimizer = optimizer.constraint( portfolio.expected_return(), ">=", 0)
            optim_portfolio_one_constraints = optimizer.run()
            variance_portfolio = compute(optim_portfolio_one_constraints.variance())
            assert len(variance_portfolio[0][0]) > 0

    def test_optimization_forecast(self):
            portfolio = Portfolio('t-1', 't', 'SPY')
            position = portfolio.add_position('GOOG', 100)
            position = portfolio.add_position('AAPL', 100)
            portfolio.settings(portfolioMetricsMode="price", resultsSamplingInterval='1m')
            optimizer = Optimizer(portfolio.variance(), direction="min")
            optimizer = optimizer.constraint(portfolio.expected_return(), ">=", 0)
            optim_portfolio_one_constraints = optimizer.run()
            variance_portfolio = compute(optim_portfolio_one_constraints.variance())
            assert len(variance_portfolio[0][0]) > 0

    def test_optimization_forecast_sampling_interval(self):
           portfolio = Portfolio( "2014-11-17 09:30:00", "2014-12-17 16:00:00", 'SPY')
           positionG = portfolio.add_position('GOOG', 200)
           positionA = portfolio.add_position('AAPL', 100)
           portfolio.settings(inputSamplingInterval='30m',resultsSamplingInterval='1d')
           forecast_object_G = Forecast(positionG.variance(),model='HAR',step ='1d')
           forecast_object_A = Forecast(positionA.variance(), model='HAR',step ='1d')
           optimizer1 = Optimizer(portfolio.variance(), direction="min")
           optimizer1=optimizer1.constraint(portfolio.log_return(),">=",0)
           optimPortfolio= optimizer1.run()
           Variance1 = compute(optimPortfolio.variance())
           optimizer2 = Optimizer(portfolio.variance(), direction="min")
           optimizer2 = optimizer2.constraint(portfolio.log_return(), ">=", 0)
           optimizer2=optimizer2.forecast("Variance",forecast_object_G)
           optimizer2=optimizer2.forecast("Variance", forecast_object_A)
           optimPortfolioForecast = optimizer2.run()
           Variance2 = compute(optimPortfolioForecast.variance())
           assert not Variance1[0][1][len(Variance1[0][1]) - 1] - Variance2[0][1][len(Variance2[0][1]) - 1] == 0





if __name__ == '__main__':
    unittest.main()