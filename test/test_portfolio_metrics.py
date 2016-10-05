import unittest
import configparser
from hft.util import *
from hft.plot import *
from hft.portfolio import *
from hft.position import *
from hft.metric import *


class TestAllPortfolioMetric(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        config = configparser.ConfigParser()
        config.read('credentials.ini')

        util_setCredentials(config['DEFAULT']['username'],
                            config['DEFAULT']['password'],
                            config['DEFAULT']['apiKey'])
        super(TestAllPortfolioMetric, self).__init__(*args, **kwargs)

    def test_portfolio_value(self):
        portfolio = Portfolio('t-1', 't', 'SPY')
        position = portfolio.add_position('GOOG', 100)
        position = portfolio.add_position('AAPL', 100)
        test=compute(portfolio.value())
        assert test[0][0][0] > 0
    def test_portfolio_expected_shortfall(self):
        portfolio = Portfolio('t-1', 't', 'SPY')
        position = portfolio.add_position('GOOG', 100)
        position = portfolio.add_position('AAPL', 100)
        test=compute(portfolio.expected_shortfall(0.95))
        assert test[0][0][0] > 0
    def test_portfolio_value_at_risk(self):
        portfolio = Portfolio('t-1', 't', 'SPY')
        position = portfolio.add_position('GOOG', 100)
        position = portfolio.add_position('AAPL', 100)
        test=compute(portfolio.value_at_risk())
        assert test[0][0][0] > 0
    def test_portfolio_alpha_exante(self):
        portfolio = Portfolio('t-1', 't', 'SPY')
        position = portfolio.add_position('GOOG', 100)
        position = portfolio.add_position('AAPL', 100)
        test=compute(portfolio.alpha_exante())
        assert test[0][0][0] > 0
    def test_portfolio_beta(self):
        portfolio = Portfolio('t-1', 't', 'SPY')
        position = portfolio.add_position('GOOG', 100)
        position = portfolio.add_position('AAPL', 100)
        test=compute(portfolio.beta())
        assert test[0][0][0] > 0
    def test_portfolio_calmar_ratio(self):
        portfolio = Portfolio('t-1', 't', 'SPY')
        position = portfolio.add_position('GOOG', 100)
        position = portfolio.add_position('AAPL', 100)
        test=compute(portfolio.calmar_ratio())
        assert test[0][0][0] > 0
    def test_portfolio_cumulant(self):
        portfolio = Portfolio('t-1', 't', 'SPY')
        position = portfolio.add_position('GOOG', 100)
        position = portfolio.add_position('AAPL', 100)
        test=compute(portfolio.cumulant(3))
        assert test[0][0][0] > 0
    def test_portfolio_down_capture_ratio(self):
        portfolio = Portfolio('t-1', 't', 'SPY')
        position = portfolio.add_position('GOOG', 100)
        position = portfolio.add_position('AAPL', 100)
        test=compute(portfolio.down_capture_ratio())
        assert test[0][0][0] > 0
    def test_portfolio_down_number_ratio(self):
        portfolio = Portfolio('t-1', 't', 'SPY')
        position = portfolio.add_position('GOOG', 100)
        position = portfolio.add_position('AAPL', 100)
        test=compute(portfolio.down_number_ratio())
        assert test[0][0][0] > 0
    def test_portfolio_down_percentage_ratio(self):
        portfolio = Portfolio('t-1', 't', 'SPY')
        position = portfolio.add_position('GOOG', 100)
        position = portfolio.add_position('AAPL', 100)
        test=compute(portfolio.down_percentage_ratio())
        assert test[0][0][0] > 0
    def test_portfolio_downside_variance(self):
        portfolio = Portfolio('t-1', 't', 'SPY')
        position = portfolio.add_position('GOOG', 100)
        position = portfolio.add_position('AAPL', 100)
        test=compute(portfolio.downside_variance(0.95))
        assert test[0][0][0] > 0
    def test_portfolio_expected_downside_return(self):
        portfolio = Portfolio('t-1', 't', 'SPY')
        position = portfolio.add_position('GOOG', 100)
        position = portfolio.add_position('AAPL', 100)
        test=compute(portfolio.expected_downside_return(0.95))
        assert test[0][0][0] > 0
    def test_portfolio_expected_return(self):
        portfolio = Portfolio('t-1', 't', 'SPY')
        position = portfolio.add_position('GOOG', 100)
        position = portfolio.add_position('AAPL', 100)
        test=compute(portfolio.expected_return())
        assert test[0][0][0] > 0
    def test_portfolio_expected_upside_return(self):
        portfolio = Portfolio('t-1', 't', 'SPY')
        position = portfolio.add_position('GOOG', 100)
        position = portfolio.add_position('AAPL', 100)
        test=compute(portfolio.expected_upside_return(0.95))
        assert test[0][0][0] > 0
    def test_portfolio_fractal_dimension(self):
        portfolio = Portfolio('t-1', 't', 'SPY')
        position = portfolio.add_position('GOOG', 100)
        position = portfolio.add_position('AAPL', 100)
        test=compute(portfolio.fractal_dimension())
        assert test[0][0][0] > 0
    def test_portfolio_gain_loss_variance_ratio(self):
        portfolio = Portfolio('t-1', 't', 'SPY')
        position = portfolio.add_position('GOOG', 100)
        position = portfolio.add_position('AAPL', 100)
        test=compute(portfolio.gain_loss_variance_ratio())
        assert test[0][0][0] > 0
    def test_portfolio_gain_variance(self):
        portfolio = Portfolio('t-1', 't', 'SPY')
        position = portfolio.add_position('GOOG', 100)
        position = portfolio.add_position('AAPL', 100)
        test=compute(portfolio.gain_variance())
        assert test[0][0][0] > 0
    def test_portfolio_hurst_exponent(self):
        portfolio = Portfolio('t-1', 't', 'SPY')
        position = portfolio.add_position('GOOG', 100)
        position = portfolio.add_position('AAPL', 100)
        test=compute(portfolio.hurst_exponent())
        assert test[0][0][0] > 0
    def test_portfolio_information_ratio(self):
        portfolio = Portfolio('t-1', 't', 'SPY')
        position = portfolio.add_position('GOOG', 100)
        position = portfolio.add_position('AAPL', 100)
        test=compute(portfolio.information_ratio())
        assert test[0][0][0] > 0
    def test_portfolio_alpha_jensens(self):
        portfolio = Portfolio('t-1', 't', 'SPY')
        position = portfolio.add_position('GOOG', 100)
        position = portfolio.add_position('AAPL', 100)
        test=compute(portfolio.alpha_jensens())
        assert test[0][0][0] > 0
    def test_portfolio_kurtosis(self):
        portfolio = Portfolio('t-1', 't', 'SPY')
        position = portfolio.add_position('GOOG', 100)
        position = portfolio.add_position('AAPL', 100)
        test=compute(portfolio.kurtosis())
        assert test[0][0][0] > 0
    def test_portfolio_loss_variance(self):
        portfolio = Portfolio('t-1', 't', 'SPY')
        position = portfolio.add_position('GOOG', 100)
        position = portfolio.add_position('AAPL', 100)
        test=compute(portfolio.loss_variance())
        assert test[0][0][0] > 0
    def test_portfolio_max_drawdown(self):
        portfolio = Portfolio('t-1', 't', 'SPY')
        position = portfolio.add_position('GOOG', 100)
        position = portfolio.add_position('AAPL', 100)
        test=compute(portfolio.max_drawdown())
        assert test[0][0][0] > 0
    def test_portfolio_mod_sharpe_ratio(self):
        portfolio = Portfolio('t-1', 't', 'SPY')
        position = portfolio.add_position('GOOG', 100)
        position = portfolio.add_position('AAPL', 100)
        test=compute(portfolio.mod_sharpe_ratio())
        assert test[0][0][0] > 0
    def test_portfolio_moment(self):
        portfolio = Portfolio('t-1', 't', 'SPY')
        position = portfolio.add_position('GOOG', 100)
        position = portfolio.add_position('AAPL', 100)
        test=compute(portfolio.moment(4))
        assert test[0][0][0] > 0
    def test_portfolio_omega_ratio(self):
        portfolio = Portfolio('t-1', 't', 'SPY')
        position = portfolio.add_position('GOOG', 100)
        position = portfolio.add_position('AAPL', 100)
        test=compute(portfolio.omega_ratio(0.95))
        assert test[0][0][0] > 0
    def test_portfolio_profit(self):
        portfolio = Portfolio('t-1', 't', 'SPY')
        position = portfolio.add_position('GOOG', 100)
        position = portfolio.add_position('AAPL', 100)
        test=compute(portfolio.profit())
        assert test[0][0][0] > 0
    def test_portfolio_rachev_ratio(self):
        portfolio = Portfolio('t-1', 't', 'SPY')
        position = portfolio.add_position('GOOG', 100)
        position = portfolio.add_position('AAPL', 100)
        test=compute(portfolio.rachev_ratio())
        assert test[0][0][0] > 0
    def test_portfolio_log_return(self):
        portfolio = Portfolio('t-1', 't', 'SPY')
        position = portfolio.add_position('GOOG', 100)
        position = portfolio.add_position('AAPL', 100)
        test=compute(portfolio.log_return())
        assert test[0][0][0] > 0
    def test_portfolio_sharpe_ratio(self):
        portfolio = Portfolio('t-1', 't', 'SPY')
        position = portfolio.add_position('GOOG', 100)
        position = portfolio.add_position('AAPL', 100)
        test=compute(portfolio.sharpe_ratio())
        assert test[0][0][0] > 0
    def test_portfolio_skewness(self):
        portfolio = Portfolio('t-1', 't', 'SPY')
        position = portfolio.add_position('GOOG', 100)
        position = portfolio.add_position('AAPL', 100)
        test=compute(portfolio.skewness())
        assert test[0][0][0] > 0
    def test_portfolio_sortino_ratio(self):
        portfolio = Portfolio('t-1', 't', 'SPY')
        position = portfolio.add_position('GOOG', 100)
        position = portfolio.add_position('AAPL', 100)
        test=compute(portfolio.sortino_ratio(0.95))
        assert test[0][0][0] > 0
    def test_portfolio_starr_ratio(self):
        portfolio = Portfolio('t-1', 't', 'SPY')
        position = portfolio.add_position('GOOG', 100)
        position = portfolio.add_position('AAPL', 100)
        test=compute(portfolio.starr_ratio())
        assert test[0][0][0] > 0
    def test_portfolio_treynor_ratio(self):
        portfolio = Portfolio('t-1', 't', 'SPY')
        position = portfolio.add_position('GOOG', 100)
        position = portfolio.add_position('AAPL', 100)
        test=compute(portfolio.treynor_ratio())
        assert test[0][0][0] > 0
    def test_portfolio_txn_costs(self):
        portfolio = Portfolio('t-1', 't', 'SPY')
        position = portfolio.add_position('GOOG', 100)
        position = portfolio.add_position('AAPL', 100)
        test=compute(portfolio.txn_costs())
        assert test[0][0][0] > 0
    def test_portfolio_up_capture_ratio(self):
        portfolio = Portfolio('t-1', 't', 'SPY')
        position = portfolio.add_position('GOOG', 100)
        position = portfolio.add_position('AAPL', 100)
        test=compute(portfolio.up_capture_ratio())
        assert test[0][0][0] > 0
    def test_portfolio_up_number_ratio(self):
        portfolio = Portfolio('t-1', 't', 'SPY')
        position = portfolio.add_position('GOOG', 100)
        position = portfolio.add_position('AAPL', 100)
        test=compute(portfolio.up_number_ratio())
        assert test[0][0][0] > 0
    def test_portfolio_up_percentage_ratio(self):
        portfolio = Portfolio('t-1', 't', 'SPY')
        position = portfolio.add_position('GOOG', 100)
        position = portfolio.add_position('AAPL', 100)
        test=compute(portfolio.up_percentage_ratio())
        assert test[0][0][0] > 0
    def test_portfolio_upside_downside_variance_ratio(self):
        portfolio = Portfolio('t-1', 't', 'SPY')
        position = portfolio.add_position('GOOG', 100)
        position = portfolio.add_position('AAPL', 100)
        test=compute(portfolio.upside_downside_variance_ratio(0.95))
        assert test[0][0][0] > 0
    def test_portfolio_upside_variance(self):
        portfolio = Portfolio('t-1', 't', 'SPY')
        position = portfolio.add_position('GOOG', 100)
        position = portfolio.add_position('AAPL', 100)
        test=compute(portfolio.upside_variance(0.95))
        assert test[0][0][0] > 0
    def test_portfolio_variance(self):
        portfolio = Portfolio('t-1', 't', 'SPY')
        position = portfolio.add_position('GOOG', 100)
        position = portfolio.add_position('AAPL', 100)
        test=compute(portfolio.variance())
        assert test[0][0][0] > 0


if __name__ == '__main__':
    unittest.main()