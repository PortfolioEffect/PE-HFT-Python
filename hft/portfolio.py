"""
This module provides a container class for storing portfolio parameters. 
"""
from position import *
import matplotlib.pyplot as plt
import sys
import numpy as np

#
# Portfolio Methods
#
class Portfolio:
    """Container class for storing portfolio parameters."""
    
    def __init__(self, fromTime=None, toTime=None, index = 'SPY', indexData = None):
        """Creates new empty Portfolio.

        Arguments:
            index: Index symbol that should be used in the Single Index Model. Defaults to "SPY".
            fromTime: Start of market data interval in "yyyy-MM-dd hh:mm:ss" format when internal market data is used. Offset from last available date/time by N days is denoted as "t-N" (e.g. "t-7" denotes offset by 7 days).
            toTime: End of market data interval in "yyyy-MM-dd hh:mm:ss" format when internal market data is used. Offset from last available date/time by N days is denoted as "t-N" (e.g. "t-7" denotes offset by 7 days).
            indexData: Vector of (time, price) observations for market index asset when external market data is used.
        Returns:
            Portfolio object.
        """
        global CLIENT_CONNECTION
        if CLIENT_CONNECTION is None:
            CLIENT_CONNECTION = util_validateConnection()

        if str(type(fromTime))=="<class 'jnius.reflect.com.portfolioeffect.quant.client.portfolio.Portfolio'>":
            portfolio_java=fromTime
        else:

         portfolio_autoclass = autoclass('com.portfolioeffect.quant.client.portfolio.Portfolio')

         if indexData is None:
             if not isinstance(fromTime, str):
                 sys.exit("fromTime should have class 'str'")
             if not isinstance(toTime, str):
                 sys.exit("toTime should have class 'str'")
             portfolio_java = portfolio_autoclass(CLIENT_CONNECTION, fromTime, toTime, index)

         else:
            if not isinstance(indexData, (list, np.ndarray)):
                sys.exit("indexData should have class 'list'")
            time_datatime = util_timezone(indexData[0])
            fromTime = time_datatime[0].strftime("%Y-%m-%d %H:%M:%S")
            toTime = time_datatime[-1].strftime("%Y-%m-%d %H:%M:%S")
            portfolio_java = portfolio_autoclass(CLIENT_CONNECTION, fromTime, toTime)
            list_long_time = util_POSIXTime_to_TLongArrayList(indexData[0])
            list_double_price = util_to_TArrayList(indexData[1], 'Double')
            portfolio_java.addIndex(list_double_price, list_long_time)

         settings_default=dict(portfolioMetricsMode="portfolio",
				windowLength = "1d",
                holdingPeriodsOnly = "false",
				shortSalesMode = "lintner",
				synchronizationModel = "true",
				jumpsModel = "moments",
                noiseModel = "true",
                fractalPriceModel = "true",
                factorModel = "sim",
                densityModel="GLD",
                driftTerm="false",
                resultsNAFilter="true",
                resultsSamplingInterval ="1s",
                inputSamplingInterval="1s",
				timeScale="1d",
				txnCostPerShare=0,
				txnCostFixed=0)
         portfolio_java.setPortfolioSettings(json.dumps(settings_default))
        self.java = portfolio_java
    
    def __call__(self):
        return
    
    def __repr__(self):
        print(self)
        return ''
    
    def __str__(self):
        util_validate()
        portfolio = self.copy()
        setting=portfolio.settings()
        print("PORTFOLIO SETTINGS")
        print('')
        print('Portfolio metrics mode '+setting['portfolioMetricsMode'])
        print('Window length  '+setting['windowLength'])
        print('Time scale  '+setting['timeScale'])
        print('Holding periods only  '+setting['holdingPeriodsOnly'])
        print('Short sales mode '+setting['shortSalesMode'])
        print('Price jumps model  '+setting['jumpsModel'])
        print('Microstructure noise model  '+setting['noiseModel'])
        print('Fractal price model  '+setting['fractalPriceModel'])
        print('Portfolio factor model  '+setting['factorModel'])
        print('Density model  '+setting['densityModel'])
        print('Drift term enabled  '+setting['driftTerm'])
        print('Results NA filter  '+setting['resultsNAFilter'])
        print('Results sampling interval  '+setting['resultsSamplingInterval'])
        print('Input sampling interval  '+setting['inputSamplingInterval'])
        print('Transaction cost per share  '+setting['txnCostPerShare'])
        print('Transaction cost fixed  '+setting['txnCostFixed'])
        print('')
        print('')

        portfolio.java.setPortfolioSettings(json.dumps({'resultsSamplingInterval':"last"}))
        portfolio.java.setPortfolioSettings(json.dumps({'resultsNAFilter':"false"}))
        positions = portfolio.java.getPositions()
        portfolio.java.createCallGroup(1 + len(positions))

        temp_portfolio = compute(portfolio.profit(), portfolio.log_return(), portfolio.value())

        printMatrix1=[["Symbol","Quantity", "Weight (in %)", "Profit", "Return (in %)", "Value", "Price"]]
        for  i in range(len(positions)):
            positionTemp = Position(positions[i], positions[i].getName(), Portfolio(fromTime=positions[i].getPortfolio()))
            temp_position = compute(positionTemp.quantity(), positionTemp.weight(), positionTemp.profit(),positionTemp.log_return(), positionTemp.value(), positionTemp.price())
            temp=[positionTemp.symbol]
            temp.append(str(temp_position[0][1][0]))
            temp.append(str(round(temp_position[1][1][0]*100,3)))
            temp.append(str(round(temp_position[2][1][0],3)))
            temp.append(str(round(temp_position[3][1][0],3)*100))
            temp.append(str(round(temp_position[4][1][0],3)*100))
            temp.append(str(round(temp_position[5][1][0],3)))
            printMatrix1.append(temp)
        printMatrix2=[["  Profit", "  Return (in %)", "  Value"]]

        temp=[]
        temp.append(str(round(temp_portfolio[0][1][0], 3)))
        temp.append(str(round(temp_portfolio[1][1][0], 3) * 100))
        temp.append(str(round(temp_portfolio[2][1][0], 3)))
        printMatrix2.append(temp)

        print("POSITION SUMMARY")
        util_print_table(printMatrix1)
        print('')
        print('')
        print("PORTFOLIO SUMMARY")
        print('')
        util_print_table(printMatrix2)
        return ''
    
    def copy(self):
        portfolio_autoclass = autoclass('com.portfolioeffect.quant.client.portfolio.Portfolio')
        portf = Portfolio(fromTime=portfolio_autoclass(self.java))
        return portf
    
    def plot(self,**kwargs):
        util_validate()
        plot_keys = kwargs.keys()

        if 'title' in plot_keys:
            title = kwargs['title']
        else:
            title = ""

        if 'subtitle' in plot_keys:
            subtitle = kwargs['subtitle']
        else:
            subtitle = ""

        if 'line_size' in plot_keys:
            line_size = kwargs['line_size']
        else:
            line_size = 2

        if 'title_size' in plot_keys:
            title_size = kwargs['title_size']
        else:
            title_size = 17

        if 'date_formatter' in plot_keys:
            date_formatter = kwargs['date_formatter']
        else:
            date_formatter = '%b-%d %H-%M'

        if 'plot_size' in plot_keys:
            plot_size = kwargs['title_size']
        else:
            plot_size = (6, 6)

        def format_date(x, pos=None):
            thisind = np.clip(int(x + 0.5), 0, N - 1)
            return times[thisind].strftime(date_formatter)
        portfolioTemp = self.copy()
        ax1=plt.subplot2grid((4,2), (0,0), colspan=2)
        ax4=plt.subplot2grid((4,2), (1,0))
        ax5=plt.subplot2grid((4,2), (1,1))
        ax2=plt.subplot2grid((4,2), (2,0), colspan=2)
        ax3=plt.subplot2grid((4,2), (3,0), colspan=2)

        symbols =portfolioTemp.symbols()
        temp=compute(portfolioTemp.value(),portfolioTemp.expected_return(),portfolioTemp.variance())
        times = util_timezone(temp[0][0])
        N = len(temp[0][1])
        ind = np.arange(N)  # the evenly spaced plot indices
        ax1.plot(ind, temp[0][1], lw=line_size)
        ax1.xaxis.set_major_formatter(ticker.FuncFormatter(format_date))
        ax1.set_title('Portfolio value ($)', y=0.99, fontsize=17)
        ax1.grid(True)

        times = util_timezone(temp[1][0])
        N = len(temp[1][1])
        ind = np.arange(N)  # the evenly spaced plot indices
        ax2.plot(ind, temp[1][1], lw=line_size)
        ax2.xaxis.set_major_formatter(ticker.FuncFormatter(format_date))
        ax2.set_title("Portfolio Expected Return", y=0.99, fontsize=17)
        ax2.grid(True)

        times = util_timezone(temp[2][0])
        N = len(temp[2][1])
        ind = np.arange(N)  # the evenly spaced plot indices
        ax3.plot(ind, temp[2][1], lw=line_size)
        ax3.xaxis.set_major_formatter(ticker.FuncFormatter(format_date))
        ax3.set_title("Portfolio Variance", y=0.99, fontsize=17)
        ax3.grid(True)


        portfolioTemp.settings(samplingInterval='last')
        positions = portfolioTemp.java.getPositions()
        PositionWeight=[0]*len(symbols)
        PositionProfit=[0]*len(symbols)
        for i in range(0, len(positions)):
            positionTemp = Position(positions[i], positions[i].getName(), Portfolio(fromTime=positions[i].getPortfolio()))
            symbols[i] = positionTemp.symbol

            PositionWeight[i]=compute(positionTemp.weight())[0][1]
            PositionProfit[i]=compute(positionTemp.profit())[0][1]

        ax4.barh(range(0, len(PositionWeight)), np.double(PositionWeight),0.4,align='center')
        ax4.set_yticks(range(0, len(PositionWeight)), minor=False)
        ax4.set_yticklabels(symbols, fontdict=None, minor=False)
        ax4.set_title("Position Weight", y=0.99, fontsize=17)
        ax4.grid(True)
        ax5.barh(range(0, len(PositionProfit)), np.double(PositionProfit),0.4,align='center')
        ax5.set_yticks(range(0, len(PositionProfit)), minor=False)
        ax5.set_yticklabels(symbols, fontdict=None, minor=False)
        ax5.set_title("Position Profit ($)", y=0.99, fontsize=17)
        ax5.grid(True)

      #  plt.suptitle(title, y=0.99, fontsize=title_size)
      #  plt.title(subtitle, fontsize=title_size - 5)
        plt.tight_layout()
        plt.rcParams['figure.figsize'] = plot_size
        plt.show()

    
    def value(self):
        """Creates monetary value of a portfolio from the beginning of the holding period.
        
        Arguments:
          None
        Returns:
          Metric object
        """        
        return util_metric(self, {'metric': 'VALUE'})
    
    def log_return(self):
        """Creates portfolio log_return from the beginning of the holding period.
        
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
        """Returns profit for the selected symbol in the portfolio.
        
        Arguments:
          None
        Returns:
          Metric object
        """
        return util_metric(self, {'metric': 'PROFIT'})
    
    def beta(self):
        """Creates portfolio beta (market sensitivity) according to the Single Index Model.

        Arguments:
          None
        Returns:
          Metric object
        """
        return util_metric(self, {'metric': 'BETA'})
    
    def alpha_exante(self):
        """Creates portfolio alpha (ex-ante) according to the Single Index Model.

        Arguments:
          None
        Returns:
          Metric object
        """
        return util_metric(self, {'metric': 'ALPHA'})
    
    def variance(self):
        """Creates variance of portfolio returns.

        Arguments:
          None
        Returns:
          Metric object
        """
        return util_metric(self, {'metric': 'VARIANCE'})
    
    def max_drawdown(self):
        """Creates maximum drawdown of portfolio returns.

        Arguments:
          None
        Returns:
          Metric object
        """
        return util_metric(self, {'metric': 'MAX_DRAWDOWN'})
    
    def calmar_ratio(self):
        """Creates Calmar ratio (cumulative return to maximum drawdown) of a portfolio

        Arguments:
          None
        Returns:
          Metric object
        """
        return util_metric(self, {'metric': 'CALMAR_RATIO'})
    
    def value_at_risk(self, confidenceInterval=0.95):
        """Creates portfolio Value-at-Risk at a given confidence interval. Computation employs distribution's skewness and kurtosis to account for non-normality.

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
        """Creates portfolio conditional Value-at-Risk (Expected Tail Loss) at a given confidence interval. Computation employs distribution's skewness and kurtosis to account for non-normality.

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
        """Creates modified Sharpe ratio of a portfolio at a given confidence interval. Computation employs distribution skewness and kurtosis to account for non-normality.

        Arguments:
          None.
          confidenceInterval: confidence interval (in decimals) to be used as a cut-off point.
        Returns:
            Metric object
        """

        return util_metric(self, {'metric': 'SHARPE_RATIO_MOD', 'confidenceInterval': confidenceInterval})
    
    def starr_ratio(self, confidenceInterval=0.95):
        """Creates Stable Tail Adjusted Return Ratio (STARR) of a portfolio at a given confidence interval. Computation employs distribution's skewness and kurtosis to account for non-normality.

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
        """Creates Sharpe Ratio of a portfolio.

        Arguments:
          None
        Returns:
          Metric object
        """
        return util_metric(self, {'metric': 'SHARPE_RATIO'})
    
    def treynor_ratio(self):
        """Creates Treynor Ratio of a portfolio.

        Arguments:
          None
        Returns:
          Metric object
        """        
        return util_metric(self, {'metric': 'TREYNOR_RATIO'})
    
    def skewness(self):
        """Creates skewness of portfolio returns.

        Arguments:
          None
        Returns:
          Metric object
        """                
        return util_metric(self, {'metric': 'SKEWNESS'})
    
    def kurtosis(self):
        """Creates kurtosis of portfolio returns.

        Arguments:
          None
        Returns:
          Metric object
        """                        
        return util_metric(self, {'metric': 'KURTOSIS'})
    
    def information_ratio(self):
        """Creates information ratio of a portfolio.

        Arguments:
          None
        Returns:
          Metric object
        """            
        return util_metric(self, {'metric': 'INFORMATION_RATIO'})
    
    def alpha_jensens(self):
        """Creates portfolio Jensen's alpha (excess return) according to the Single Index Model.

        Arguments:
          None
        Returns:
          Metric object
        """                     
        return util_metric(self, {'metric': 'ALPHA_JENSEN'})
    
    def omega_ratio(self, thresholdReturn):
        """Creates Omega Ratio of a portfolio. Computation employs distribution's skewness and kurtosis to account for non-normality.

        Arguments:
          None
          thresholdReturn: return value to be used as a cut-off point
        Returns:
          Metric object
        """    
        return util_metric(self, {'metric': 'OMEGA_RATIO', 'thresholdReturn': thresholdReturn})
    
    def rachev_ratio(self, confidenceIntervalA=0.95, confidenceIntervalB=0.95):
        """Creates Rachev ratio of a portfolio at given confidence intervals. Computation employs distribution skewness and kurtosis to account for non-normality.

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
        """Creates gain variance of portfolio returns.

        Arguments:
          None
        Returns:
          Metric object
        """       
        return util_metric(self, {'metric': 'GAIN_VARIANCE'})
    
    def loss_variance(self):
        """Creates loss variance of portfolio returns.

        Arguments:
          None
        Returns:
          Metric object
        """         
        return util_metric(self, {'metric': 'LOSS_VARIANCE'})
    
    def downside_variance(self, thresholdReturn):
        """Creates downside variance of portfolio returns.

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
        """Creates upside variance of portfolio returns.

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
        """Creates portfolio cumulative expected return below a certain threshold.

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
        """Creates portfolio cumulative expected return above a certain threshold.

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
        """Creates portfolio Hurst exponent as a weighted sum of the Hurst exponents of its position returns.

        Arguments:
          None
        Returns:
          Metric object
        """    
        return util_metric(self, {'metric': 'HURST_EXPONENT'})
    
    def fractal_dimension(self):
        """Creates portfolio fractal dimension as a weighted sum of fractal dimensions of its position returns.

        Arguments:
          None
        Returns:
          Metric object
        """    
        return util_metric(self, {'metric': 'FRACTAL_DIMENSION'})
    
    def txn_costs(self):
        """Creates monetary value of accumulated portfolio transactional costs.

        Arguments:
          None
        Returns:
          Metric object
        """         
        return util_metric(self, {'metric': 'TRANSACTION_COSTS_SIZE'})
    
    def sortino_ratio(self, thresholdReturn):
        """Creates Sortino ratio of a portfolio.

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
        """Creates upside to downside variance ratio of a portfolio.

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
        """Creates gain to loss variance ratio of portfolio returns.

        Arguments:
          None
        Returns:
          Metric object
        """    
        return util_metric(self, {'metric': 'GAIN_LOSS_VARIANCE_RATIO'})
    
    def down_capture_ratio(self):
        """Creates down capture ratio of a portfolio.

        Arguments:
          None
        Returns:
          Metric object
        """    
        return util_metric(self, {'metric': 'DOWN_CAPTURE_RATIO'})
    
    def up_capture_ratio(self):
        """Creates up capture ratio of a portfolio.

        Arguments:
          None
        Returns:
          Metric object
        """    
        return util_metric(self, {'metric': 'UP_CAPTURE_RATIO'})
    
    def down_number_ratio(self):
        """Creates down number ratio of a portfolio.

        Arguments:
          None
        Returns:
          Metric object
        """    
        return util_metric(self, {'metric': 'DOWN_NUMBER_RATIO'})
    
    def up_number_ratio(self):
        """Creates up number ratio of a portfolio.

        Arguments:
          None
        Returns:
          Metric object
        """    
        return util_metric(self, {'metric': 'UP_NUMBER_RATIO'})
    
    def down_percentage_ratio(self):
        """Creates down percentage ratio of portfolio returns.

        Arguments:
          None
        Returns:
          Metric object
        """    
        return util_metric(self, {'metric': 'DOWN_PERCENTAGE_RATIO'})
    
    def up_percentage_ratio(self):
        """Creates up percentage ratio of a portfolio.

        Arguments:
          None
        Returns:
          Metric object
        """            
        return util_metric(self, {'metric': 'UP_PERCENTAGE_RATIO'})
    
    def cumulant(self,order):
        """Creates N-th cumulant of portfolio return distribution.

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
        """Creates N-th order central moment of portfolio return distribution.

        Arguments:
          None
          order: moment order (from 1 to 4)
        Returns:
          Metric object
        """
        if not isinstance(order, int):
            sys.exit("order should have class 'int'")
        return util_metric(self, {'metric': 'MOMENT'+str(order)})

    
    def symbols(self):
       """Returns a list of portfolio symbols with non-zero weights.

       Arguments:
         None
       Returns:
        List of position symbols with non-zero weights
       """
       util_validate()
       result = self.java.getSymbols()
       return result

    def get_position(self, symbol):
        """Returns position for a given symbol if this position is found inside a given portfolio

       Arguments:
         symbol: unique identifier of an instrument
       Returns:
        Object of class position for a given symbol, if found in the portfolio
       """
        if not isinstance(symbol, str):
            sys.exit("symbol should have class 'str'")
        positions = self.java.getPositions()
        symbols = self.java.getSymbols()
        num = symbols.index(symbol)
        position = Position(positions[num], symbol, self)
        return position

    def symbols_available(self):
        """Returns a list of symbols. 

       Arguments:
         None
       Returns:
        List of symbols, exchanges and description
       """
        result_metric = self.java.getAllSymbolsList()
        result = util_getResult(result_metric,False)
        return result

    def add_position(self, symbol, quantity=None, time=None, priceData=None):
        """Adds position to an existing portfolio

       Arguments:
         symbol: unique identifier of the instrument
         quantity: one dimensional vector of position quantities or an integer number if quantity is constant
         time: one dimensional vector of time values either as "yyyy-MM-dd hh:mm:ss" string or in milliseconds since the beginning of epoch.
       Returns:
         None
       """
        if not isinstance(symbol, str):
            sys.exit("symbol should have class 'str'")
        DateTimeUtil = autoclass('com.portfolioeffect.quant.client.util.DateTimeUtil');
        Position_autoclass = autoclass('com.portfolioeffect.quant.client.portfolio.Position')
        if priceData is None:
            if isinstance(quantity, (list, tuple)):
                list_quntity = util_to_TArrayList(quantity, "Int")
            else:
                list_quntity = quantity
            if time is not None:
                if not isinstance(time[0],long):
                    list_time = DateTimeUtil.toPOSIXTimeTLongArrayList(time);
                else:
                    list_time = util_POSIXTime_to_TLongArrayList(time)
                result = Position_autoclass(self.java, symbol, list_quntity, list_time);
            else:
                result = Position_autoclass(self.java, symbol, list_quntity);
        else:
            list_long_time = util_POSIXTime_to_TLongArrayList(priceData[0])
            list_double_price = util_to_TArrayList(priceData[1], 'Double')
            list_float_price = util_to_TArrayList(priceData[1], 'Float')
            if isinstance(quantity, (list, tuple)):
                list_quntity = util_to_TArrayList(quantity, "Int")
            else:
                list_quntity = quantity
                list_double_price = list_float_price
            if time is not None:
                if not isinstance(time[0],long):
                    list_time = DateTimeUtil.toPOSIXTimeTLongArrayList(time);
                else:
                    list_time = util_POSIXTime_to_TLongArrayList(time)
                result = Position_autoclass(self.java, symbol, list_double_price, list_long_time, list_quntity,
                                            list_time);
            else:
                result = Position_autoclass(self.java, symbol, list_double_price, list_quntity, list_long_time);

        position = Position(result, symbol, self)
        return position

    def remove_position (self, symbol):
        """Removes position from an existing portfolio.

       Arguments:
         symbol: unique identifier of the instrument
       Returns:
         None
       """
        if not isinstance(symbol, str):
            sys.exit("symbol should have class 'str'")
        self.removePositionQuantity(symbol)
        self.removePositionPrice(symbol)

    def settings_default(self):
        """Advanced settings that regulate how porfolio metrics are computed, returned and stored. Default:portfolioMetricsMode="portfolio", windowLength = "1d",  holdingPeriodsOnly = FALSE, shortSalesMode = "lintner", synchronizationModel = TRUE, jumpsModel = "moments", noiseModel = TRUE, fractalPriceModel=TRUE, factorModel = "sim", densityModel="GLD", driftTerm=FALSE, resultsNAFilter= TRUE, resultsSamplingInterval = "1s", inputSamplingInterval="1s", timeScale="1d", txnCostPerShare=0, txnCostFixed=0
       
       Arguments:
         None
       Returns:
         None
       """          
        self.settings(portfolioMetricsMode="portfolio",
                           windowLength="1d",
                           holdingPeriodsOnly="false",
                           shortSalesMode="lintner",
                           synchronizationModel="true",
                           jumpsModel="moments",
                           noiseModel="true",
                           fractalPriceModel="true",
                           factorModel="sim",
                           densityModel="GLD",
                           driftTerm="false",
                           resultsNAFilter="true",
                           resultsSamplingInterval="1s",
                           inputSamplingInterval="1s",
                           timeScale="1d",
                           txnCostPerShare=0,
                           txnCostFixed=0)

    def settings(self, *args, **kwargs):
        """Advanced settings that regulate how porfolio metrics are computed, returned and stored. Default: portfolioMetricsMode="portfolio", windowLength = "1d", holdingPeriodsOnly = FALSE, shortSalesMode = "lintner", jumpsModel = "moments", noiseModel = TRUE, fractalPriceModel=TRUE, factorModel = "sim", densityModel="GLD", driftTerm=TRUE, resultsSamplingInterval = "1s", inputSamplingInterval="none", timeScale="1d", txnCostPerShare=0, txnCostFixed=0

        Arguments:
            portfolio: Portfolio object created using Portfolio( ) function
            One of the following portfolio settings:
                "portfolioMetricsMode" - Used to select method of computing portfolio metrics. Available modes are: "portfolio" - risk and performance metrics are computed based on the history of position rebalancing (see windowLength parameter) and should be used to backtest and compare trading strategies of different frequency and style, "price" - metrics are always computed without a history of previous rebalancing (classic interpretation). Defaults to "portfolio".
                "windowLength" - Rolling window length for metric estimations and position rebalancing history. Available interval values are: "Xs" - seconds, "Xm" - minutes, "Xh" - hours, "Xd" - trading days (6.5 hours in a trading day), "Xw" - weeks (5 trading days in 1 week), "Xmo" - month (21 trading day in 1 month), "Xy" - years (256 trading days in 1 year), "all" - all observations are used. Default value is "1d" - one trading day .
                "holdingPeriodsOnly - Used when portfolioMetricsMode = "portfolio". Defaults to FALSE, which means that trading strategy risk and performance metrics will be scaled to include intervals when trading strategy did not have market exposure. When TRUE, trading strategy metrics are scaled based on actual holding intervals when there was exposure to the market.
                "shortSalesMode" - Used to specify how position weights are computed. Available modes are: "lintner" - the sum of absolute weights is equal to 1 (Lintner assumption), "markowitz" - the sum of weights must equal to 1 (Markowitz assumption). Defaults to "lintner", which implies that the sum of absolute weights is used to normalize investment weights.
                "jumpsModel" - Used to select jump filtering mode when computing return statistics. Available modes are: "none" - price jumps are not filtered anywhere, "moments" - price jumps are filtered only when computing moments (variance, skewness, kurtosis) and derived metrics, "all" - price jumps are filtered everywhere. Defaults to "moments", which implies that only return moments and related metrics would be using jump-filtered returns in their calculations.
                "noiseModel" - Used to enable microstructure noise model of distribution returns. Defaults to TRUE, which implies that microstructure effects are modeled and resulting HF noise is removed from metric calculations.
                "fractalPriceModel" - Used to enable mono-fractal price assumptions (fGBM) when time scaling return moments. Defaults to TRUE, which implies that computed Hurst exponent is used to scale return moments. When FALSE, price is assumed to follow regular GBM with Hurst exponent = 0.5.
                "factorModel" - Used to select factor model for computing portfolio metrics. Available models are: "sim" - portfolio metrics are computed using the Single Index Model, "direct" - portfolio metrics are computed using portfolio value itself. Defaults to "sim", which implies that the Single Index Model is used to compute portfolio metrics.
                "densityModel" - Used to select density approximation model of return distribution. Available models are: "GLD" - Generalized Lambda Distribution, "CORNER_FISHER" - Corner-Fisher approximation, "NORMAL" - Gaussian distribution. Defaults to "GLD", which would fit a broad range of distribution shapes.
                "driftTerm" - Used to enable drift term (expected return) when computing probability density approximation and related metrics (e.g. CVaR, Omega Ratio, etc.). Defaults to FALSE, which implies that distribution is centered around zero return.
                "resultsNAFilter" - Used to enable filtering of NA values in computed results. Defaults to TRUE, which implies that output results have all NA values removed.
                "resultsSamplingInterval" - Interval to be used for sampling computed results before returning them to the caller. Available interval values are: "Xs" - seconds, "Xm" - minutes, "Xh" - hours, "Xd" - trading days (6.5 hours in a trading day), "Xw" - weeks (5 trading days in 1 week), "Xmo" - month (21 trading day in 1 month), "Xy" - years (256 trading days in 1 year), "last" - last result in a series is returned, "none" - no sampling. Large sampling interval would produce smaller vector of results and would require less time spent on data transfer. Default value of "1s" indicates that data is returned for every second during trading hours.
                "inputSamplingInterval" - Interval to be used as a minimum step for sampling input prices. Available interval values are: "Xs" - seconds, "Xm" - minutes, "Xh" - hours, "Xd" - trading days (6.5 hours in a trading day), "Xw" - weeks (5 trading days in 1 week), "Xmo" - month (21 trading day in 1 month), "Xy" - years (256 trading days in 1 year), "none" - no sampling. Default value is "none", which indicates that no sampling is applied.
                "timeScale" - Interval to be used for scaling return distribution statistics and producing metrics forecasts at different horizons. Available interval values are: "Xs" - seconds, "Xm" - minutes, "Xh" - hours, "Xd" - trading days (6.5 hours in a trading day), "Xw" - weeks (5 trading days in 1 week), "Xmo" - month (21 trading day in 1 month), "Xy" - years (256 trading days in 1 year), "all" - actual interval specified in during portfolio creation. Default value is "1d" - one trading day.
                "txnCostPerShare" - Amount of transactional costs per share. Defaults to 0.
                "txnCostFixed" - Amount of fixed costs per transaction. Defaults to 0.
        Returns:
            None
        """
        if len(args) > 0:
            if isinstance(args[0], dict):
                kwargs = args[0]
        util_validate()
        self.java.setPortfolioSettings(json.dumps(kwargs))

        setting = dict()
        setting["portfolioMetricsMode"] = self.java.getParam("portfolioMetricsMode")
        setting["windowLength"] = self.java.getParam("windowLength")
        setting["holdingPeriodsOnly"] = self.java.getParam("isHoldingPeriodEnabled")
        setting["shortSalesMode"] = self.java.getParam("shortSalesMode")
        setting["jumpsModel"] = self.java.getParam("jumpsModel")
        setting["noiseModel"] = self.java.getParam("isNoiseModelEnabled")
        setting["fractalPriceModel"] = self.java.getParam("isFractalPriceModelEnabled")
        setting["factorModel"] = self.java.getParam("factorModel")
        setting["resultsNAFilter"] = self.java.getParam("isNaNFiltered")
        setting["resultsSamplingInterval"] = self.java.getParam("samplingInterval")
        setting["inputSamplingInterval"] = self.java.getParam("priceSamplingInterval")
        setting["timeScale"] = self.java.getParam("timeScale")
        setting["driftTerm"] = self.java.getParam("isDriftEnabled")
        setting["txnCostPerShare"] = self.java.getParam("txnCostPerShare")
        setting["txnCostFixed"] = self.java.getParam("txnCostFixed")
        setting["densityModel"] = self.java.getParam("densityApproxModel")
        return setting



