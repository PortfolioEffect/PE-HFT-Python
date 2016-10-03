"""
This module provides a container class for storing position parameters. 
"""

from __init__ import *
from portfolio import *
from util import *
from metric import *
from plot import *


#
# Position Methods
#

class Position:
    """Container class for storing position parameters."""
    
    def __init__(self, java,symbol,portfolio):
        self.java = java
        self.symbol = symbol
        self.portfolio = portfolio
    
    def __repr__(self):
        print self
        return ''
    
    def __str__(self):
        util_validate()
        portfolio = self.portfolio.copy()

        portfolio.java.setPortfolioSettings(json.dumps({'resultsSamplingInterval':"last"}))
        portfolio.java.setPortfolioSettings(json.dumps({'resultsNAFilter':"false"}))
        positionTemp = portfolio.get_position(self.symbol)

        printMatrix1=[["Symbol","Quantity", "Weight (in %)", "Profit", "Return (in %)", "Value", "Price"]]
        temp_position = compute(positionTemp.quantity(), positionTemp.weight(), positionTemp.profit(),positionTemp.log_return(), positionTemp.value(), positionTemp.price())
        temp=[positionTemp.symbol]
        temp.append(str(temp_position[0][1][0]))
        temp.append(str(round(temp_position[1][1][0]*100,3)))
        temp.append(str(round(temp_position[2][1][0],3)))
        temp.append(str(round(temp_position[3][1][0],3)*100))
        temp.append(str(round(temp_position[4][1][0],3)*100))
        temp.append(str(round(temp_position[5][1][0],3)))
        printMatrix1.append(temp)

        print "POSITION SUMMARY"
        print ''
        util_print_table(printMatrix1)
        return ''

    def plot(self,bw=False):
        util_validate()
        def format_date(x, pos=None):
            thisind = np.clip(int(x + 0.5), 0, N - 1)
            return times[thisind].strftime('%b-%d %H-%M')
        ax1=plt.subplot2grid((4,1), (0,0))
        ax2=plt.subplot2grid((4, 1), (1, 0))
        ax3=plt.subplot2grid((4,1), (2,0))
        ax4=plt.subplot2grid((4,1), (3,0))

        temp = compute(self.value(), self.weight(), self.expected_return(), self.variance())

        times = util_timezone(temp[0][0])
        N = len(temp[0][1])
        ind = np.arange(N)  # the evenly spaced plot indices
        ax1.plot(ind, temp[0][1], lw=2)
        ax1.xaxis.set_major_formatter(ticker.FuncFormatter(format_date))
        ax1.set_title('Position value ($)', y=0.99, fontsize=17)
        ax1.grid(True)

        times = util_timezone(temp[1][0])
        N = len(temp[1][1])
        ind = np.arange(N)  # the evenly spaced plot indices
        ax2.plot(ind, temp[1][1], lw=2)
        ax2.xaxis.set_major_formatter(ticker.FuncFormatter(format_date))
        ax2.set_title("Position weight (%)", y=0.99, fontsize=17)
        ax2.grid(True)

        times = util_timezone(temp[2][0])
        N = len(temp[2][1])
        ind = np.arange(N)  # the evenly spaced plot indices
        ax3.plot(ind, temp[2][1], lw=2)
        ax3.xaxis.set_major_formatter(ticker.FuncFormatter(format_date))
        ax3.set_title("Position Expected Return", y=0.99, fontsize=17)
        ax3.grid(True)

        times = util_timezone(temp[3][0])
        N = len(temp[3][1])
        ind = np.arange(N)  # the evenly spaced plot indices
        ax4.plot(ind, temp[3][1], lw=2)
        ax4.xaxis.set_major_formatter(ticker.FuncFormatter(format_date))
        ax4.set_title("Position Variance", y=0.99, fontsize=17)
        ax4.grid(True)

        plt.tight_layout()
        plt.show()
    
    def __call__ (self):
        return 1
    
    def value(self):
        """Creates monetary value of a position from the beginning of the holding period.
        
        Arguments:
          None
        Returns:
          Metric object
        Example:
          timeStart="2014-10-02 09:30:00"
          timeEnd="2014-10-03 16:00:00"
          portfolio=Portfolio(timeStart,timeEnd,"SPY")
          portfolio.settings(portfolioMetricsMode="price", jumpsModel='all')
          positionAAPL=portfolio.add_position("AAPL",100)
          positionAAPL.value()  
        """
        return util_metric(self, {'metric': 'VALUE'})
    
    def log_return(self):
        """Creates position log_return from the beginning of the holding period.
        
        Arguments:
          None
        Returns:
          Metric object
        """
        return util_metric(self, {'metric': 'RETURN'})
    
    def expected_return(self):
        """Creates portfolio cumulative expected return.
        
        Arguments:
          None
        Returns:
          Metric object
        """
        return util_metric(self, {'metric': 'EXPECTED_RETURN'})
    
    def profit(self):
        """Returns profit for the selected symbol in the position.
        
        Arguments:
          None
        Returns:
          Metric object
        """
        return util_metric(self, {'metric': 'PROFIT'})
    
    def beta(self):
        """Creates position beta (market sensitivity) according to the Single Index Model.
        
        Arguments:
          None
        Returns:
          Metric object
        """
        return util_metric(self, {'metric': 'BETA'})
    
    def alpha_exante(self):
        """Creates position alpha (ex-ante) according to the Single Index Model.

        Arguments:
          None
        Returns:
          Metric object
        """
        return util_metric(self, {'metric': 'ALPHA'})
    
    def variance(self):
        """Creates variance of position returns.

        Arguments:
          None
        Returns:
          Metric object
        """
        return util_metric(self, {'metric': 'VARIANCE'})
    
    def max_drawdown(self):
        """Creates maximum drawdown of position returns.

        Arguments:
          None
        Returns:
          Metric object
        """
        return util_metric(self, {'metric': 'MAX_DRAWDOWN'})
    
    def calmar_ratio(self):
        """Creates Calmar ratio (cumulative return to maximum drawdown) of a position

        Arguments:
          None
        Returns:
          Metric object
        """
        return util_metric(self, {'metric': 'CALMAR_RATIO'})
    
    def value_at_risk(self, confidenceInterval=0.95):
        """Creates position Value-at-Risk at a given confidence interval. Computation employs distribution's skewness and kurtosis to account for non-normality.

        Arguments:
          None
          confidenceInterval: confidence interval (in decimals) to be used as a cut-off point.
        Returns:
            Metric object
        """
        if not isinstance(confidenceInterval, float):
            sys.exit("confidenceInterval should have class 'float'")
        return util_metric(self, {'metric': 'VAR', 'confidenceInterval': confidenceInterval})
    
    def expected_shortfall(self, confidenceInterval=0.95):
        """Creates position conditional Value-at-Risk (Expected Tail Loss) at a given confidence interval. Computation employs distribution's skewness and kurtosis to account for non-normality.

        Arguments:
          None    
          confidenceInterval: confidence interval (in decimals) to be used as a cut-off point.
        Returns:
            Metric object
        """
        if not isinstance(confidenceInterval, float):
            sys.exit("confidenceInterval should have class 'float'")
        return util_metric(self, {'metric': 'CVAR', 'confidenceInterval': confidenceInterval})
    
    def mod_sharpe_ratio(self, confidenceInterval=0.95):
        """Creates modified Sharpe ratio of a position at a given confidence interval. Computation employs distribution skewness and kurtosis to account for non-normality.

        Arguments:
          None.
          confidenceInterval: confidence interval (in decimals) to be used as a cut-off point.
        Returns:
            Metric object
        """
        if not isinstance(confidenceInterval, float):
            sys.exit("confidenceInterval should have class 'float'")
        return util_metric(self, {'metric': 'SHARPE_RATIO_MOD', 'confidenceInterval': confidenceInterval})
    
    def starr_ratio(self, confidenceInterval=0.95):
        """Creates Stable Tail Adjusted Return Ratio (STARR) of a position at a given confidence interval. Computation employs distribution's skewness and kurtosis to account for non-normality.

        Arguments:
          None.
          confidenceInterval: confidence interval (in decimals) to be used as a cut-off point.
        Returns:
          Metric object
        """
        if not isinstance(confidenceInterval, float):
            sys.exit("confidenceInterval should have class 'float'")
        return util_metric(self, {'metric': 'STARR_RATIO', 'confidenceInterval': confidenceInterval})
    
    def sharpe_ratio(self):
        """Creates Sharpe Ratio of a position.

        Arguments:
          None
        Returns:
          Metric object
        """
        return util_metric(self, {'metric': 'SHARPE_RATIO'})
    
    def treynor_ratio(self):
        """Creates Treynor Ratio of a position.

        Arguments:
          None
        Returns:
          Metric object
        """        
        return util_metric(self, {'metric': 'TREYNOR_RATIO'})

    def skewness(self):
        """Creates skewness of position returns.

        Arguments:
          None
        Returns:
          Metric object
        """            
        return util_metric(self, {'metric': 'SKEWNESS'})
    
    def kurtosis(self):
        """Creates kurtosis of position returns.

        Arguments:
          None
        Returns:
          Metric object
        """                    
        return util_metric(self, {'metric': 'KURTOSIS'})
    
    def information_ratio(self):
        """Creates information ratio of a position.

        Arguments:
          None
        Returns:
          Metric object
        """         
        return util_metric(self, {'metric': 'INFORMATION_RATIO'})
    
    def alpha_jensens(self):
        """Creates position Jensen's alpha (excess return) according to the Single Index Model.

        Arguments:
          None
        Returns:
          Metric object
        """                 
        return util_metric(self, {'metric': 'ALPHA_JENSEN'})
    
    def omega_ratio(self, thresholdReturn):
        """Creates Omega Ratio of a position. Computation employs distribution's skewness and kurtosis to account for non-normality.

        Arguments:
          None
          thresholdReturn: return value to be used as a cut-off point
        Returns:
          Metric object
        """
        if not isinstance(thresholdReturn, float):
            sys.exit("thresholdReturn should have class 'float'")
        return util_metric(self, {'metric': 'OMEGA_RATIO', 'thresholdReturn': thresholdReturn})
    
    def rachev_ratio(self, confidenceIntervalA=0.95, confidenceIntervalB=0.95):
        """Creates Rachev ratio of a position at given confidence intervals. Computation employs distribution skewness and kurtosis to account for non-normality.

        Arguments:
          None
          confidenceIntervalA: confidence interval (in decimals) to be used as a cut-off point in the numerator
          confidenceIntervalB: confidence interval (in decimals) to be used as a cut-off point in the denominator
        Returns:
          Metric object
        """
        if not isinstance(confidenceIntervalA, float):
            sys.exit("confidenceIntervalA should have class 'float'")
        if not isinstance(confidenceIntervalB, float):
            sys.exit("confidenceIntervalB should have class 'float'")
        return util_metric(self, {'metric': 'RACHEV_RATIO', 'confidenceIntervalAlpha': confidenceIntervalA,
                                   'confidenceIntervalBeta': confidenceIntervalB})
    
    def gain_variance(self):
        """Creates gain variance of position returns.

        Arguments:
          None
        Returns:
          Metric object
        """   
        return util_metric(self, {'metric': 'GAIN_VARIANCE'})
    
    def loss_variance(self):
        """Creates loss variance of position returns.

        Arguments:
          None
        Returns:
          Metric object
        """         
        return util_metric(self, {'metric': 'LOSS_VARIANCE'})
    
    def downside_variance(self, thresholdReturn):
        """Creates downside variance of position returns.

        Arguments:
          None
          thresholdReturn: return value to be used as a cut-off poin
        Returns:
          Metric object
        """
        if not isinstance(thresholdReturn, float):
            sys.exit("thresholdReturn should have class 'float'")
        return util_metric(self, {'metric': 'DOWNSIDE_VARIANCE', 'thresholdReturn': thresholdReturn})

    def upside_variance(self, thresholdReturn):
        """Creates upside variance of position returns.

        Arguments:
          None
          thresholdReturn: return value to be used as a cut-off poin
        Returns:
          Metric object
        """
        if not isinstance(thresholdReturn, float):
            sys.exit("thresholdReturn should have class 'float'")
        return util_metric(self, {'metric': 'UPSIDE_VARIANCE', 'thresholdReturn': thresholdReturn})

    def expected_downside_return(self, thresholdReturn):
        """Creates position cumulative expected return below a certain threshold.

        Arguments:
          None
          thresholdReturn: return value to be used as a cut-off poin
        Returns:
          Metric object
        """
        if not isinstance(thresholdReturn, float):
            sys.exit("thresholdReturn should have class 'float'")
        return util_metric(self, {'metric': 'EXPECTED_DOWNSIDE_THRESHOLD_RETURN', 'thresholdReturn': thresholdReturn})

    def expected_upside_return(self, thresholdReturn):
        """Creates position cumulative expected return above a certain threshold.

        Arguments:
          None
          thresholdReturn: return value to be used as a cut-off poin
        Returns:
          Metric object
        """
        if not isinstance(thresholdReturn, float):
            sys.exit("thresholdReturn should have class 'float'")
        return util_metric(self, {'metric': 'EXPECTED_UPSIDE_THRESHOLD_RETURN', 'thresholdReturn': thresholdReturn})
    
    def hurst_exponent(self):
        """Creates position Hurst exponent as a weighted sum of the Hurst exponents of its position returns.

        Arguments:
          None
        Returns:
          Metric object
        """
        return util_metric(self, {'metric': 'HURST_EXPONENT'})
    
    def fractal_dimension(self):
        """Creates position fractal dimension as a weighted sum of fractal dimensions of its position returns.

        Arguments:
          None
        Returns:
          Metric object
        """
        return util_metric(self, {'metric': 'FRACTAL_DIMENSION'})
    
    def txn_costs(self):
        """Creates monetary value of accumulated position transactional costs.

        Arguments:
          None
        Returns:
          Metric object
        """        
        return util_metric(self, {'metric': 'TRANSACTION_COSTS_SIZE'})
    
    def sortino_ratio(self, thresholdReturn):
        """Creates Sortino ratio of a position.

        Arguments:
          None
          thresholdReturn: return value to be used as a cut-off point
        Returns:
          Metric object
        """
        if not isinstance(thresholdReturn, float):
            sys.exit("thresholdReturn should have class 'float'")
        return util_metric(self, {'metric': 'SORTINO_RATIO', 'thresholdReturn': thresholdReturn})
    
    def upside_downside_variance_ratio(self, thresholdReturn):
        """Creates upside to downside variance ratio of a position.

        Arguments:
          None
          thresholdReturn: return value to be used as a cut-off point
        Returns:
          Metric object
        """
        if not isinstance(thresholdReturn, float):
            sys.exit("thresholdReturn should have class 'float'")
        return util_metric(self, {'metric': 'UPSIDE_DOWNSIDE_VARIANCE_RATIO', 'thresholdReturn': thresholdReturn})
    
    def gain_loss_variance_ratio(self):
        """Creates gain to loss variance ratio of position returns.

        Arguments:
          None
        Returns:
          Metric object
        """
        return util_metric(self, {'metric': 'GAIN_LOSS_VARIANCE_RATIO'})
    
    def down_capture_ratio(self):
        """Creates down capture ratio of a position.

        Arguments:
          None
        Returns:
          Metric object
        """
        return util_metric(self, {'metric': 'DOWN_CAPTURE_RATIO'})
    
    def up_capture_ratio(self):
        """Creates up capture ratio of a position.

        Arguments:
          None
        Returns:
          Metric object
        """
        return util_metric(self, {'metric': 'UP_CAPTURE_RATIO'})
    
    def down_number_ratio(self):
        """Creates down number ratio of a position.

        Arguments:
          None
        Returns:
          Metric object
        """
        return util_metric(self, {'metric': 'DOWN_NUMBER_RATIO'})
    
    def up_number_ratio(self):
        """Creates up number ratio of a position.

        Arguments:
          None
        Returns:
          Metric object
        """
        return util_metric(self, {'metric': 'UP_NUMBER_RATIO'})
    
    def down_percentage_ratio(self):
        """Creates down percentage ratio of position returns.

        Arguments:
          None
        Returns:
          Metric object
        """
        return util_metric(self, {'metric': 'DOWN_PERCENTAGE_RATIO'})
    
    def up_percentage_ratio(self):
        """Creates up percentage ratio of a position.

        Arguments:
          None
        Returns:
          Metric object
        """        
        return util_metric(self, {'metric': 'UP_PERCENTAGE_RATIO'})
    
    def cumulant(self,order):
        """Creates N-th cumulant of position return distribution.

        Arguments:
          None
          order: moment order (3 or 4)
        Returns:
          Metric object
        """
        if not isinstance(order, int):
            sys.exit("order should have class 'int'")
        return util_metric(self, {'metric': 'CUMULANT'+str(order)})
    
    def moment(self,order):
        """Creates N-th order central moment of position return distribution.

        Arguments:
          None
          order: moment order (from 1 to 4)
        Returns:
          Metric object
        """
        if not isinstance(order, int):
            sys.exit("order should have class 'int'")
        return util_metric(self, {'metric': 'MOMENT'+str(order)})
    
    def set_quantity(self, quantity):
        """Sets new position quantity.

        Arguments:
          quantity: one dimensional vector of position quantities or an integer number if quantity is constan
        Returns:
          Metric object
        """
        if not isinstance(quantity, int):
            sys.exit("quantity should have class 'int'")
        self.java.setPositionQuantity(quantity)
    
    def quantity(self):
        """Returns total number of shares associated with the given symbol in this portfolio.

        Arguments:
          None
        Returns:
          Metric object
        """        
        return util_metric(self, {'metric': 'QUANTITY'})
    
    def price(self):
        """Returns position price.

        Arguments:
          asset: Position object created using position_add( ) function
        Returns:
          Metric object
        """        
        return util_metric(self, {'metric': 'PRICE'})
    
    def weight(self):
        """Creates ratio of a monetary position value to the monetary value of the whole portfolio. Expressed in decimal points of portfolio value.

        Arguments:
          asset: Position object created using position_add( ) function
        Returns:
          Metric object
        """                
        return util_metric(self, {'metric': 'WEIGHT'})
    
    def return_autocovariance(self, lag=10):
        """Creates autocovariance of position returns for a certain time lag.

        Arguments:
          lag: time lag (in seconds) between observations in question
        Returns:
          Metric object
        """
        if not isinstance(lag, int):
            sys.exit("lag should have class 'int'")
        return util_metric(self, {'metric': 'RETURN_AUTOCOVARIANCE', 'lag': lag})
    
    def correlation(self,positionB):
        """Creates correlation between positionA and positionB.

        Arguments:
          positionA: Position object created using position_add( ) function
          positionB: Position object created using position_add( ) function
        Returns:
          Metric object
        """
        if not positionB.__class__.__name__ == 'Position':
            sys.exit("positionB should have class 'Position'")
        DateTimeUtil = autoclass('com.portfolioeffect.quant.client.util.LazyMetricBuilder')
        builder = DateTimeUtil(json.dumps( {'metric': 'CORRELATION'}))
        result = builder.build(self.java,positionB.java)
        metric = Metric(result)
        return metric
    
    def covariance(self, positionB):
        """Creates covariance between positionA and positionB.

        Arguments:
          positionA: Position object created using position_add( ) function
          positionB: Position object created using position_add( ) function
        Returns:
          Metric object
        """
        if not positionB.__class__.__name__ == 'Position':
            sys.exit("positionB should have class 'Position'")
        DateTimeUtil = autoclass('com.portfolioeffect.quant.client.util.LazyMetricBuilder')
        builder = DateTimeUtil(json.dumps( {'metric': 'COVARIANCE'}))
        result = builder.build(self.java,positionB.java)
        metric = Metric(result)
        return metric




