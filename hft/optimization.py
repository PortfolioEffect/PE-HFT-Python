"""
This module provides a container for storing optimization goals and constraints..
"""
from __init__ import *
from util import *
from metric import *
from portfolio import *
from position import *
from forecast import *
import matplotlib.pyplot as plt
import numpy as np
import sys

#
# Optimizer Methods
#
class Optimizer:
    """Class for storing optimization goals and constraints."""
    
    def __init__(self,goal,direction = ["min", "max"],approxError = 1e-12,optimumProbability = 0.99):
        if not goal.__class__.__name__ == 'Metric':
            sys.exit("goal should have class 'Metric'")
        if not isinstance(direction, (str, list)):
            sys.exit("direction should have class 'str' or 'list'")
        if not isinstance(approxError, float):
            sys.exit("approxError should have class 'float'")
        if not isinstance(optimumProbability, float):
            sys.exit("optimumProbability should have class 'float'")
        portfolio_java = goal.java.getPortfolio()
        # if (not (direction[0] in ["min", "max"])):
        #    sys.exit("Direction not specified")
        direction = {
            "min": "minimize",
            "max": "maximize"}[direction[0] if isinstance(direction, list) else direction]

        if portfolio_java.getParam("portfolioMetricsMode") == 'portfolio':
            path = autoclass("com.portfolioeffect.quant.client.portfolio.optimizer.StrategyOptimizer")
            isStrategyOptimizer = True
        else:
            path = autoclass("com.portfolioeffect.quant.client.portfolio.optimizer.PortfolioOptimizer")
            isStrategyOptimizer = False

        optimizer_java = path(portfolio_java)
        optimizer_java.setOptimizationGoal(goal.java, direction)
        optimizer_java.setErrorInDecimalPoints(approxError)
        optimizer_java.setGlobalOptimumProbability(optimumProbability)
        if isStrategyOptimizer:
            optimizer_java.setForecastBuilder(Forecast(goal).java)
            optimizer_java.setForecastStep(portfolio_java.getSamplingInterval())

        self.java = optimizer_java
        self.portfolio = portfolio_java

    def run(self):
         """Runs portfolio optimization procedure and returns corresponding optimal portfolio.
        
         Arguments:
           None
         Returns:
           Optimal portfolio object
         """
         # util_validate()
         result = self.java.getOptimizedPortfolio()
         return Portfolio(fromTime=util_getResult(result, False)[0])

    def constraint(self, constraintMertic, constraintType, constraintValue):
        """Adds portfolio optimization constraint restricting optimal portfolio's beta to a certain range.
        
        Arguments:
          constraintMertic: object of class metric to be used for computing optimization constraint
          constraintType: optimization constraint type:
              "=" - an equality constraint,
              ">=" - an inclusive lower bound constraint,
              "<=" - an inclusive upper bound constraint
          constraintValue: value to be used as a constraint boundary
        Returns:
          Object of class optimizer
        """
        if not constraintMertic.__class__.__name__ == 'Metric':
            sys.exit("constraintMertic should have class 'Metric'")
        if not isinstance(constraintValue, (float, list, int)):
            sys.exit("constraintValue should have class 'float','int' or 'list'")
        if not isinstance(constraintType, str):
            sys.exit("constraintType should have class 'str'")
        constraintTypeFinal = constraintType
        self.java.addConstraint(constraintMertic.java, constraintTypeFinal, constraintValue)


        return self

    def forecast(self, metricType, forecast):
        """Sets user-defined forecasted values for a given metric and returns modified optimizer object. By default value of the metric at time "t" is used as a forecast for "t+1".
        
        Arguments:
          metricType: choose forecast metric type:
              "Beta" - position beta,
              "Variance" - position variance,
              "ExpReturn" - position expected return,
              "Cumulant3" - position 3-th cumulant,
              "Cumulant4" - position 4-th cumulant
          forecast: object of class metric-class( ) or forecast-class( )
        Returns:
          Optimizer object
        """
        if not isinstance(metricType, str):
            sys.exit("metricType should have class 'str'")
        if not ((forecast.__class__.__name__ == 'Metric') or (forecast.__class__.__name__ == 'Forecast')):
            sys.exit("forecast should have class 'Metric' or 'Forecast'")
        if (forecast.__class__.__name__ == 'Forecast'):
            {"ExpReturn": self.java.setExpectedReturnForecastBuilder(forecast.java),
                "Beta": self.java.setBetaForecastBuilder(forecast.java),
                "Variance": self.java.setVarianceForecastBuilder(forecast.java),
                "Cumulant3": self.java.setCumulant3ForecastBuilder(forecast.java),
                "Cumulant4": self.java.setCumulant4ForecastBuilder(forecast.java)}[metricType]
        else:
            if forecast.__class__.__name__ == 'Metric':
                if forecast.java.__class__.__name__ == Metric([ range(10),range(10)] , "SPY").java.__class__.__name__:
                    symbol = forecast.java.getDescription()
                else:
                    symbol = forecast.java.getSymbol()

                data = compute(forecast)[0]
                forecastedValues = autoclass("com.portfolioeffect.quant.client.portfolio.optimizer.ForecastedValues")
                forecastedValues = forecastedValues(self.portfolio)

                result={
                    "ExpReturn":  forecastedValues.setSymbolForecastedExpReturn(symbol, util_to_TArrayList(data[1], 'Double'), util_POSIXTime_to_TLongArrayList(data[0])),
#                    "Beta":  forecastedValues.setSymbolForecastedBeta(symbol, util_to_TArrayList(data[1], 'Double'), util_POSIXTime_to_TLongArrayList(data[0])),
                    "Variance": forecastedValues.setSymbolForecastedVariance(symbol, util_to_TArrayList(data[1], 'Double'), util_POSIXTime_to_TLongArrayList(data[0])),
                    "Cumulant3":  forecastedValues.setSymbolForecastedCumulant3(symbol, util_to_TArrayList(data[1], 'Double'), util_POSIXTime_to_TLongArrayList(data[0])),
                    "Cumulant4":  forecastedValues.setSymbolForecastedCumulant4(symbol, util_to_TArrayList(data[1], 'Double'), util_POSIXTime_to_TLongArrayList(data[0]))}[metricType]
#                result=forecastedValues.setSymbolForecastedExpReturn(symbol, util_to_TArrayList(data[1], 'Double'), util_POSIXTime_to_TLongArrayList(data[0]))
                util_checkErrors(result)
                self.java.setForecastedValue(forecastedValues)
        return self