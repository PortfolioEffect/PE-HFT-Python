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
                            config['DEFAULT']['apiKey'])
        super(TestSettingsMethods, self).__init__(*args, **kwargs)

    def test_settings(self):
        portfolio = Portfolio('2015-06-12 09:30:00', '2015-06-14 16:00:00', 'SPY')
        positionG = portfolio.add_position( 'GOOG', 100)
        positionA = portfolio.add_position( 'AAPL', 100)
        portfolio.settings( resultsSamplingInterval='30m')
        Variance = compute(portfolio.variance())
        assert len(Variance[0][1]) == 13

    def test_getSettings(self):
        portfolio = Portfolio('2015-06-12 09:30:00', '2015-06-14 16:00:00', 'SPY')
        positionG = portfolio.add_position( 'GOOG', 100)
        positionA = portfolio.add_position( 'AAPL', 100)
        portfolio.settings( resultsSamplingInterval='30m')
        settings = portfolio.settings()
        portfolio.settings( resultsSamplingInterval='1m')
        portfolio.settings( settings)
        settings = portfolio.settings()
        assert settings['resultsSamplingInterval'] == '30m'

    def test_settings_portfolioMetricsMode(self):
        portfolio1 = Portfolio('2015-06-12 09:30:00', '2015-06-14 16:00:00', 'SPY')
        positionG = portfolio1.add_position( 'GOOG', 100)
        positionA = portfolio1.add_position( 'AAPL', 100)
        portfolio1.settings( portfolioMetricsMode='portfolio')
        portfolio2 = Portfolio('2015-06-12 09:30:00', '2015-06-14 16:00:00', 'SPY')
        positionG = portfolio2.add_position( 'GOOG', 100)
        positionA = portfolio2.add_position( 'AAPL', 100)
        portfolio2.settings( portfolioMetricsMode='price')
        Variance1 = compute(portfolio1.variance())
        Variance2 = compute(portfolio2.variance())
        assert not Variance1[0][1][len(Variance1[0][1]) - 1] - Variance2[0][1][len(Variance2[0][1]) - 1] == 0

    def test_settings_windowLength(self):
        portfolio1 = Portfolio('2015-06-12 09:30:00', '2015-06-20 16:00:00', 'SPY')
        positionG = portfolio1.add_position( 'GOOG', 100)
        positionA = portfolio1.add_position( 'AAPL', 100)
        portfolio1.settings( windowLength='1d')
        portfolio2 = Portfolio('2015-06-12 09:30:00', '2015-06-20 16:00:00', 'SPY')
        positionG = portfolio2.add_position( 'GOOG', 100)
        positionA = portfolio2.add_position( 'AAPL', 100)
        portfolio2.settings( windowLength='10d')
        Variance1 = compute(portfolio1.variance())
        Variance2 = compute(portfolio2.variance())
        assert not Variance1[0][1][len(Variance1[0][1]) - 1] - Variance2[0][1][len(Variance2[0][1]) - 1] == 0

    def test_settings_jumpsModel(self):
        portfolio1 = Portfolio('2015-06-12 09:30:00', '2015-06-14 16:00:00', 'SPY')
        positionG = portfolio1.add_position( 'GOOG', 100)
        positionA = portfolio1.add_position( 'AAPL', 100)
        portfolio1.settings( jumpsModel='moments')
        portfolio2 = Portfolio('2015-06-12 09:30:00', '2015-06-14 16:00:00', 'SPY')
        positionG = portfolio2.add_position( 'GOOG', 100)
        positionA = portfolio2.add_position( 'AAPL', 100)
        portfolio2.settings( jumpsModel='none')
        Variance1 = compute(portfolio1.variance())
        Variance2 = compute(portfolio2.variance())
        assert not Variance1[0][1][len(Variance1[0][1]) - 1] - Variance2[0][1][len(Variance2[0][1]) - 1] == 0

    def test_settings_noiseModel(self):
        portfolio1 = Portfolio('2015-06-12 09:30:00', '2015-06-14 16:00:00', 'SPY')
        positionG = portfolio1.add_position( 'GOOG', 100)
        positionA = portfolio1.add_position( 'AAPL', 100)
        portfolio1.settings( noiseModel='true')
        portfolio2 = Portfolio('2015-06-12 09:30:00', '2015-06-14 16:00:00', 'SPY')
        positionG = portfolio2.add_position( 'GOOG', 100)
        positionA = portfolio2.add_position( 'AAPL', 100)
        portfolio2.settings( noiseModel='false')
        Variance1 = compute(portfolio1.variance())
        Variance2 = compute(portfolio2.variance())
        assert not Variance1[0][1][len(Variance1[0][1]) - 1] - Variance2[0][1][len(Variance2[0][1]) - 1] == 0

    def test_settings_fractalPriceModel(self):
        portfolio1 = Portfolio('2015-06-12 09:30:00', '2015-06-14 16:00:00', 'SPY')
        positionG = portfolio1.add_position( 'GOOG', 100)
        positionA = portfolio1.add_position( 'AAPL', 100)
        portfolio1.settings( fractalPriceModel='true')
        portfolio2 = Portfolio('2015-06-12 09:30:00', '2015-06-14 16:00:00', 'SPY')
        positionG = portfolio2.add_position( 'GOOG', 100)
        positionA = portfolio2.add_position( 'AAPL', 100)
        portfolio2.settings( fractalPriceModel='false')
        Variance1 = compute(portfolio1.variance())
        Variance2 = compute(portfolio2.variance())
        assert not Variance1[0][1][len(Variance1[0][1]) - 1] - Variance2[0][1][len(Variance2[0][1]) - 1] == 0

    def test_settings_driftTerm(self):
        portfolio1 = Portfolio('2015-06-12 09:30:00', '2015-06-24 16:00:00', 'SPY')
        positionG = portfolio1.add_position( 'GOOG', 100)
        positionA = portfolio1.add_position( 'AAPL', 100)
        portfolio1.settings( driftTerm='true')
        portfolio2 = Portfolio('2015-06-12 09:30:00', '2015-06-24 16:00:00', 'SPY')
        positionG = portfolio2.add_position( 'GOOG', 100)
        positionA = portfolio2.add_position( 'AAPL', 100)
        portfolio2.settings( driftTerm='false')
        expected_shortfall1 = compute(portfolio1.expected_shortfall(0.95))
        expected_shortfall2 = compute(portfolio2.expected_shortfall(0.95))
        assert not expected_shortfall1[0][1][len(expected_shortfall1[0][1]) - 1] - expected_shortfall2[0][1][
            len(expected_shortfall2[0][1]) - 1] == 0

    def test_settings_inputSamplingInterval(self):
        portfolio1 = Portfolio('2015-06-12 09:30:00', '2015-06-14 16:00:00', 'SPY')
        positionG = portfolio1.add_position( 'GOOG', 100)
        positionA = portfolio1.add_position( 'AAPL', 100)
        portfolio1.settings( inputSamplingInterval='1m')
        portfolio2 = Portfolio('2015-06-12 09:30:00', '2015-06-14 16:00:00', 'SPY')
        positionG = portfolio2.add_position( 'GOOG', 100)
        positionA = portfolio2.add_position( 'AAPL', 100)
        portfolio2.settings( inputSamplingInterval='1s')
        Variance1 = compute(portfolio1.variance())
        Variance2 = compute(portfolio2.variance())
        assert not Variance1[0][1][len(Variance1[0][1]) - 1] - Variance2[0][1][len(Variance2[0][1]) - 1] == 0

    def test_settings_timeScale(self):
        portfolio1 = Portfolio('2015-06-12 09:30:00', '2015-06-14 16:00:00', 'SPY')
        positionG = portfolio1.add_position( 'GOOG', 100)
        positionA = portfolio1.add_position( 'AAPL', 100)
        portfolio1.settings( timeScale='1d')
        portfolio2 = Portfolio('2015-06-12 09:30:00', '2015-06-14 16:00:00', 'SPY')
        positionG = portfolio2.add_position( 'GOOG', 100)
        positionA = portfolio2.add_position( 'AAPL', 100)
        portfolio2.settings( timeScale='2d')
        Variance1 = compute(portfolio1.variance())
        Variance2 = compute(portfolio2.variance())
        assert not Variance1[0][1][len(Variance1[0][1]) - 1] - Variance2[0][1][len(Variance2[0][1]) - 1] == 0

    def test_settings_holdingPeriodsOnly(self):
        portfolio1 = Portfolio("2014-10-01 09:30:00", "2014-10-02 16:00:00", 'SPY')
        positionA = portfolio1.add_position( 'AAPL', quantity=[0, 300, 150, 0],
                                 time=["2014-09-30 09:30:00", "2014-10-01 09:30:00", "2014-10-01 15:30:00",
                                       "2014-10-02 11:30:00"])
        portfolio1.settings( holdingPeriodsOnly='true')
        portfolio2 = Portfolio("2014-10-01 09:30:00", "2014-10-02 16:00:00", 'SPY')
        positionA = portfolio2.add_position( 'AAPL', quantity=[0, 300, 150, 0],
                                 time=["2014-09-30 09:30:00", "2014-10-01 09:30:00", "2014-10-01 15:30:00",
                                       "2014-10-02 11:30:00"])
        portfolio2.settings( holdingPeriodsOnly='false')
        Variance1 = compute(portfolio1.variance())
        Variance2 = compute(portfolio2.variance())
        assert not Variance1[0][1][len(Variance1[0][1]) - 1] - Variance2[0][1][len(Variance2[0][1]) - 1] == 0

    def test_settings_shortSalesMode(self):
        portfolio1 = Portfolio('2015-06-12 09:30:00', '2015-06-14 16:00:00', 'SPY')
        positionG = portfolio1.add_position( 'GOOG', -100)
        positionA = portfolio1.add_position( 'AAPL', 100)
        portfolio1.settings( shortSalesMode="markowitz")
        portfolio2 = Portfolio('2015-06-12 09:30:00', '2015-06-14 16:00:00', 'SPY')
        positionG = portfolio2.add_position( 'GOOG', -100)
        positionA = portfolio2.add_position( 'AAPL', 100)
        portfolio2.settings( shortSalesMode="lintner")
        Variance1 = compute(portfolio1.variance())
        Variance2 = compute(portfolio2.variance())
        assert not Variance1[0][1][len(Variance1[0][1]) - 1] - Variance2[0][1][len(Variance2[0][1]) - 1] == 0

    def test_settings_densityModel(self):
        portfolio1 = Portfolio('2015-06-12 09:30:00', '2015-06-14 16:00:00', 'SPY')
        positionG = portfolio1.add_position( 'GOOG', 100)
        positionA = portfolio1.add_position( 'AAPL', 100)
        portfolio1.settings( densityModel="NORMAL")
        portfolio2 = Portfolio('2015-06-12 09:30:00', '2015-06-14 16:00:00', 'SPY')
        positionG = portfolio2.add_position( 'GOOG', 100)
        positionA = portfolio2.add_position( 'AAPL', 100)
        portfolio2.settings( densityModel="GLD")
        expected_shortfall1 = compute(portfolio1.expected_shortfall(0.95))
        expected_shortfall2 = compute(portfolio2.expected_shortfall(0.95))
        assert not expected_shortfall1[0][1][len(expected_shortfall1[0][1]) - 1] - expected_shortfall2[0][1][
            len(expected_shortfall2[0][1]) - 1] == 0

    def test_settings_factorModel(self):
        portfolio1 = Portfolio('2015-06-12 09:30:00', '2015-06-14 16:00:00', 'SPY')
        positionG = portfolio1.add_position( 'GOOG', 100)
        positionA = portfolio1.add_position( 'AAPL', 100)
        portfolio1.settings( factorModel="sim")
        portfolio2 = Portfolio('2015-06-12 09:30:00', '2015-06-14 16:00:00', 'SPY')
        positionG = portfolio2.add_position( 'GOOG', 100)
        positionA = portfolio2.add_position( 'AAPL', 100)
        portfolio2.settings( factorModel="direct")
        Variance1 = compute(portfolio1.variance())
        Variance2 = compute(portfolio2.variance())
        assert not Variance1[0][1][len(Variance1[0][1]) - 1] - Variance2[0][1][len(Variance2[0][1]) - 1] == 0

    def test_settings_txnCostPerShare(self):
        portfolio1 = Portfolio("2014-10-01 09:30:00", "2014-10-02 16:00:00", 'SPY')
        positionA = portfolio1.add_position( 'AAPL', quantity=[0, 300, 150, 0],
                                 time=["2014-09-30 09:30:00", "2014-10-01 09:30:00", "2014-10-01 15:30:00",
                                       "2014-10-02 11:30:00"])
        portfolio1.settings( txnCostPerShare=0.005)
        portfolio2 = Portfolio('2015-06-12 09:30:00', '2015-06-14 16:00:00', 'SPY')
        positionA = portfolio2.add_position( 'AAPL', quantity=[0, 300, 150, 0],
                                 time=["2014-09-30 09:30:00", "2014-10-01 09:30:00", "2014-10-01 15:30:00",
                                       "2014-10-02 11:30:00"])
        portfolio2.settings( txnCostPerShare=0.001)
        txn_costs1 = compute(portfolio1.txn_costs())
        txn_costs2 = compute(portfolio2.txn_costs())
        assert not txn_costs1[0][1][len(txn_costs1[0][1]) - 1] - txn_costs2[0][1][len(txn_costs2[0][1]) - 1] == 0

if __name__ == '__main__':
    unittest.main()