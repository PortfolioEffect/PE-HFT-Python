import unittest
import configparser
from hft.util import *
from hft.plot import *
from hft.portfolio import *
from hft.position import *
from hft.metric import *


class TestAllPositionMetric(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        config = configparser.ConfigParser()
        config.read('credentials.ini')

        util_setCredentials(config['DEFAULT']['username'],
                            config['DEFAULT']['password'],
                            config['DEFAULT']['apiKey'])
        super(TestAllPositionMetric, self).__init__(*args, **kwargs)

    def test_position_value(self):
        portfolio = Portfolio('t-1', 't', 'SPY')
        positionG = portfolio.add_position( 'GOOG', 100)
        positionA = portfolio.add_position( 'AAPL', 100)
        test=compute(positionA.value())
        assert test[0][0][0] > 0
    def test_position_expected_shortfall(self):
        portfolio = Portfolio('t-1', 't', 'SPY')
        positionG = portfolio.add_position( 'GOOG', 100)
        positionA = portfolio.add_position( 'AAPL', 100)
        test=compute(positionA.expected_shortfall(0.95))
        assert test[0][0][0] > 0
    def test_position_value_at_risk(self):
        portfolio = Portfolio('t-1', 't', 'SPY')
        positionG = portfolio.add_position( 'GOOG', 100)
        positionA = portfolio.add_position( 'AAPL', 100)
        test=compute(positionA.value_at_risk())
        assert test[0][0][0] > 0
    def test_position_alpha_exante(self):
        portfolio = Portfolio('t-1', 't', 'SPY')
        positionG = portfolio.add_position( 'GOOG', 100)
        positionA = portfolio.add_position( 'AAPL', 100)
        test=compute(positionA.alpha_exante())
        assert test[0][0][0] > 0
    def test_position_beta(self):
        portfolio = Portfolio('t-1', 't', 'SPY')
        positionG = portfolio.add_position( 'GOOG', 100)
        positionA = portfolio.add_position( 'AAPL', 100)
        test=compute(positionA.beta())
        assert test[0][0][0] > 0
    def test_position_calmar_ratio(self):
        portfolio = Portfolio('t-1', 't', 'SPY')
        positionG = portfolio.add_position( 'GOOG', 100)
        positionA = portfolio.add_position( 'AAPL', 100)
        test=compute(positionA.calmar_ratio())
        assert test[0][0][0] > 0
    def test_position_cumulant(self):
        portfolio = Portfolio('t-1', 't', 'SPY')
        positionG = portfolio.add_position( 'GOOG', 100)
        positionA = portfolio.add_position( 'AAPL', 100)
        test=compute(positionA.cumulant(3))
        assert test[0][0][0] > 0
    def test_position_down_capture_ratio(self):
        portfolio = Portfolio('t-1', 't', 'SPY')
        positionG = portfolio.add_position( 'GOOG', 100)
        positionA = portfolio.add_position( 'AAPL', 100)
        test=compute(positionA.down_capture_ratio())
        assert test[0][0][0] > 0
    def test_position_down_number_ratio(self):
        portfolio = Portfolio('t-1', 't', 'SPY')
        positionG = portfolio.add_position( 'GOOG', 100)
        positionA = portfolio.add_position( 'AAPL', 100)
        test=compute(positionA.down_number_ratio())
        assert test[0][0][0] > 0
    def test_position_down_percentage_ratio(self):
        portfolio = Portfolio('t-1', 't', 'SPY')
        positionG = portfolio.add_position( 'GOOG', 100)
        positionA = portfolio.add_position( 'AAPL', 100)
        test=compute(positionA.down_percentage_ratio())
        assert test[0][0][0] > 0
    def test_position_downside_variance(self):
        portfolio = Portfolio('t-1', 't', 'SPY')
        positionG = portfolio.add_position( 'GOOG', 100)
        positionA = portfolio.add_position( 'AAPL', 100)
        test=compute(positionA.downside_variance(0.95))
        assert test[0][0][0] > 0
    def test_position_expected_downside_return(self):
        portfolio = Portfolio('t-1', 't', 'SPY')
        positionG = portfolio.add_position( 'GOOG', 100)
        positionA = portfolio.add_position( 'AAPL', 100)
        test=compute(positionA.expected_downside_return(0.95))
        assert test[0][0][0] > 0
    def test_position_expected_return(self):
        portfolio = Portfolio('t-1', 't', 'SPY')
        positionG = portfolio.add_position( 'GOOG', 100)
        positionA = portfolio.add_position( 'AAPL', 100)
        test=compute(positionA.expected_return())
        assert test[0][0][0] > 0
    def test_position_expected_upside_return(self):
        portfolio = Portfolio('t-1', 't', 'SPY')
        positionG = portfolio.add_position( 'GOOG', 100)
        positionA = portfolio.add_position( 'AAPL', 100)
        test=compute(positionA.expected_upside_return(0.95))
        assert test[0][0][0] > 0
    def test_position_fractal_dimension(self):
        portfolio = Portfolio('t-1', 't', 'SPY')
        positionG = portfolio.add_position( 'GOOG', 100)
        positionA = portfolio.add_position( 'AAPL', 100)
        test=compute(positionA.fractal_dimension())
        assert test[0][0][0] > 0
    def test_position_gain_loss_variance_ratio(self):
        portfolio = Portfolio('t-1', 't', 'SPY')
        positionG = portfolio.add_position( 'GOOG', 100)
        positionA = portfolio.add_position( 'AAPL', 100)
        test=compute(positionA.gain_loss_variance_ratio())
        assert test[0][0][0] > 0
    def test_position_gain_variance(self):
        portfolio = Portfolio('t-1', 't', 'SPY')
        positionG = portfolio.add_position( 'GOOG', 100)
        positionA = portfolio.add_position( 'AAPL', 100)
        test=compute(positionA.gain_variance())
        assert test[0][0][0] > 0
    def test_position_hurst_exponent(self):
        portfolio = Portfolio('t-1', 't', 'SPY')
        positionG = portfolio.add_position( 'GOOG', 100)
        positionA = portfolio.add_position( 'AAPL', 100)
        test=compute(positionA.hurst_exponent())
        assert test[0][0][0] > 0
    def test_position_information_ratio(self):
        portfolio = Portfolio('t-1', 't', 'SPY')
        positionG = portfolio.add_position( 'GOOG', 100)
        positionA = portfolio.add_position( 'AAPL', 100)
        test=compute(positionA.information_ratio())
        assert test[0][0][0] > 0
    def test_position_alpha_jensens(self):
        portfolio = Portfolio('t-1', 't', 'SPY')
        positionG = portfolio.add_position( 'GOOG', 100)
        positionA = portfolio.add_position( 'AAPL', 100)
        test=compute(positionA.alpha_jensens())
        assert test[0][0][0] > 0
    def test_position_kurtosis(self):
        portfolio = Portfolio('t-1', 't', 'SPY')
        positionG = portfolio.add_position( 'GOOG', 100)
        positionA = portfolio.add_position( 'AAPL', 100)
        test=compute(positionA.kurtosis())
        assert test[0][0][0] > 0
    def test_position_loss_variance(self):
        portfolio = Portfolio('t-1', 't', 'SPY')
        positionG = portfolio.add_position( 'GOOG', 100)
        positionA = portfolio.add_position( 'AAPL', 100)
        test=compute(positionA.loss_variance())
        assert test[0][0][0] > 0
    def test_position_max_drawdown(self):
        portfolio = Portfolio('t-1', 't', 'SPY')
        positionG = portfolio.add_position( 'GOOG', 100)
        positionA = portfolio.add_position( 'AAPL', 100)
        test=compute(positionA.max_drawdown())
        assert test[0][0][0] > 0
    def test_position_mod_sharpe_ratio(self):
        portfolio = Portfolio('t-1', 't', 'SPY')
        positionG = portfolio.add_position( 'GOOG', 100)
        positionA = portfolio.add_position( 'AAPL', 100)
        test=compute(positionA.mod_sharpe_ratio())
        assert test[0][0][0] > 0
    def test_position_moment(self):
        portfolio = Portfolio('t-1', 't', 'SPY')
        positionG = portfolio.add_position( 'GOOG', 100)
        positionA = portfolio.add_position( 'AAPL', 100)
        test=compute(positionA.moment(4))
        assert test[0][0][0] > 0
    def test_position_omega_ratio(self):
        portfolio = Portfolio('t-1', 't', 'SPY')
        positionG = portfolio.add_position( 'GOOG', 100)
        positionA = portfolio.add_position( 'AAPL', 100)
        test=compute(positionA.omega_ratio(0.95))
        assert test[0][0][0] > 0
    def test_position_profit(self):
        portfolio = Portfolio('t-1', 't', 'SPY')
        positionG = portfolio.add_position( 'GOOG', 100)
        positionA = portfolio.add_position( 'AAPL', 100)
        test=compute(positionA.profit())
        assert test[0][0][0] > 0
    def test_position_rachev_ratio(self):
        portfolio = Portfolio('t-1', 't', 'SPY')
        positionG = portfolio.add_position( 'GOOG', 100)
        positionA = portfolio.add_position( 'AAPL', 100)
        test=compute(positionA.rachev_ratio())
        assert test[0][0][0] > 0
    def test_position_log_return(self):
        portfolio = Portfolio('t-1', 't', 'SPY')
        positionG = portfolio.add_position( 'GOOG', 100)
        positionA = portfolio.add_position( 'AAPL', 100)
        test=compute(positionA.log_return())
        assert test[0][0][0] > 0
    def test_position_sharpe_ratio(self):
        portfolio = Portfolio('t-1', 't', 'SPY')
        positionG = portfolio.add_position( 'GOOG', 100)
        positionA = portfolio.add_position( 'AAPL', 100)
        test=compute(positionA.sharpe_ratio())
        assert test[0][0][0] > 0
    def test_position_skewness(self):
        portfolio = Portfolio('t-1', 't', 'SPY')
        positionG = portfolio.add_position( 'GOOG', 100)
        positionA = portfolio.add_position( 'AAPL', 100)
        test=compute(positionA.skewness())
        assert test[0][0][0] > 0
    def test_position_sortino_ratio(self):
        portfolio = Portfolio('t-1', 't', 'SPY')
        positionG = portfolio.add_position( 'GOOG', 100)
        positionA = portfolio.add_position( 'AAPL', 100)
        test=compute(positionA.sortino_ratio(0.95))
        assert test[0][0][0] > 0
    def test_position_starr_ratio(self):
        portfolio = Portfolio('t-1', 't', 'SPY')
        positionG = portfolio.add_position( 'GOOG', 100)
        positionA = portfolio.add_position( 'AAPL', 100)
        test=compute(positionA.starr_ratio())
        assert test[0][0][0] > 0
    def test_position_treynor_ratio(self):
        portfolio = Portfolio('t-1', 't', 'SPY')
        positionG = portfolio.add_position( 'GOOG', 100)
        positionA = portfolio.add_position( 'AAPL', 100)
        test=compute(positionA.treynor_ratio())
        assert test[0][0][0] > 0
    def test_position_txn_costs(self):
        portfolio = Portfolio('t-1', 't', 'SPY')
        positionG = portfolio.add_position( 'GOOG', 100)
        positionA = portfolio.add_position( 'AAPL', 100)
        test=compute(positionA.txn_costs())
        assert test[0][0][0] > 0
    def test_position_up_capture_ratio(self):
        portfolio = Portfolio('t-1', 't', 'SPY')
        positionG = portfolio.add_position( 'GOOG', 100)
        positionA = portfolio.add_position( 'AAPL', 100)
        test=compute(positionA.up_capture_ratio())
        assert test[0][0][0] > 0
    def test_position_up_number_ratio(self):
        portfolio = Portfolio('t-1', 't', 'SPY')
        positionG = portfolio.add_position( 'GOOG', 100)
        positionA = portfolio.add_position( 'AAPL', 100)
        test=compute(positionA.up_number_ratio())
        assert test[0][0][0] > 0
    def test_position_up_percentage_ratio(self):
        portfolio = Portfolio('t-1', 't', 'SPY')
        positionG = portfolio.add_position( 'GOOG', 100)
        positionA = portfolio.add_position( 'AAPL', 100)
        test=compute(positionA.up_percentage_ratio())
        assert test[0][0][0] > 0
    def test_position_upside_downside_variance_ratio(self):
        portfolio = Portfolio('t-1', 't', 'SPY')
        positionG = portfolio.add_position( 'GOOG', 100)
        positionA = portfolio.add_position( 'AAPL', 100)
        test=compute(positionA.upside_downside_variance_ratio(0.95))
        assert test[0][0][0] > 0
    def test_position_upside_variance(self):
        portfolio = Portfolio('t-1', 't', 'SPY')
        positionG = portfolio.add_position( 'GOOG', 100)
        positionA = portfolio.add_position( 'AAPL', 100)
        test=compute(positionA.upside_variance(0.95))
        assert test[0][0][0] > 0
    def test_position_variance(self):
        portfolio = Portfolio('t-1', 't', 'SPY')
        positionG = portfolio.add_position( 'GOOG', 100)
        positionA = portfolio.add_position( 'AAPL', 100)
        test=compute(positionA.variance())
        assert test[0][0][0] > 0
    def test_position_quantity(self):
        portfolio = Portfolio('t-1', 't', 'SPY')
        positionG = portfolio.add_position( 'GOOG', 100)
        positionA = portfolio.add_position( 'AAPL', 100)
        test=compute(positionA.quantity())
        assert test[0][0][0] > 0
    def test_position_price(self):
        portfolio = Portfolio('t-1', 't', 'SPY')
        positionG = portfolio.add_position( 'GOOG', 100)
        positionA = portfolio.add_position( 'AAPL', 100)
        test=compute(positionA.price())
        assert test[0][0][0] > 0
    def test_position_weight(self):
        portfolio = Portfolio('t-1', 't', 'SPY')
        positionG = portfolio.add_position( 'GOOG', 100)
        positionA = portfolio.add_position( 'AAPL', 100)
        test=compute(positionA.weight())
        assert test[0][0][0] > 0
    def test_position_return_autocovariance(self):
        portfolio = Portfolio('t-1', 't', 'SPY')
        positionG = portfolio.add_position( 'GOOG', 100)
        positionA = portfolio.add_position( 'AAPL', 100)
        test=compute(positionA.return_autocovariance(10))
        assert test[0][0][0] > 0
    def test_position_correlation(self):
        portfolio = Portfolio('t-1', 't', 'SPY')
        positionG = portfolio.add_position( 'GOOG', 100)
        positionA = portfolio.add_position( 'AAPL', 100)
        test=compute(positionA.correlation(positionG))
        assert test[0][0][0] > 0
    def test_position_covariance(self):
        portfolio = Portfolio('t-1', 't', 'SPY')
        positionG = portfolio.add_position( 'GOOG', 100)
        positionA = portfolio.add_position( 'AAPL', 100)
        test=compute(positionA.covariance(positionG))
        assert test[0][0][0] > 0
    def test_set_quantity(self):
        portfolio = Portfolio('t-1', 't', 'SPY')
        positionG = portfolio.add_position( 'GOOG', 100)
        positionA = portfolio.add_position( 'AAPL', 100)
        positionA.set_quantity(200)
        test=compute(positionA.quantity())
        assert test[0][1][0] == 200



if __name__ == '__main__':
    unittest.main()