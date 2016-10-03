"""
This module provides a container class for storing forecast model and its parameters. 
"""
from __init__ import *
from util import *
from metric import *
from portfolio import *
from position import *
#
# Optimizer Methods
#
class Forecast:
    """Container class for storing forecast model and its parameters."""
    def __init__(self, asset, model=["EWMA","HAR"], window="20d", step = "1d", transform = ["log","none"], seasonalityInterval="none",updateInterval="1m",valueType="forecast"):
      if not asset.__class__.__name__== 'Metric':
            sys.exit("asset should have class 'Metric'")
      if not isinstance(model, (str,list)):
            sys.exit("model should have class 'str' or 'list'")
      if not isinstance(window, str):
            sys.exit("window should have class 'str'")
      if not isinstance(step, str):
            sys.exit("step should have class 'str'")
      if not isinstance(transform, (str,list)):
            sys.exit("transform should have class 'str' or 'list'")
      if not isinstance(seasonalityInterval, str):
            sys.exit("seasonalityInterval should have class 'str'")
      if not isinstance(updateInterval, str):
            sys.exit("updateInterval should have class 'str'")
      if not isinstance(valueType, str):
            sys.exit("valueType should have class 'str'")

      forecast_builder_autoclass = autoclass("com.portfolioeffect.quant.client.util.LinearForecastBuilder")
      forecast_builder_java = forecast_builder_autoclass()
      forecast_builder_java.setTransform(transform[0] if isinstance(transform, list) else transform)
      forecast_builder_java.setRollingWindow(window)
      forecast_builder_java.setRegressionUpdateInterval(updateInterval)
      forecast_builder_java.setForecastStep(step)
      forecast_builder_java.setValueType(valueType)
      forecast_builder_java.setTimeShiftEnable(True)
      forecast_builder_java.setDependentVariable(asset.java)
      model = {
        "HAR": "[{\"windowLength\":\"1d\"},{\"windowLength\":\"5d\"},{\"windowLength\":\"21d\"}]",
        "EWMA": "[]"}[model[0] if isinstance(model, list) else model]
      forecast_builder_java.setForecastModel(model)
      if (not seasonalityInterval == "none"):
        forecast_builder_java.setSeasonInterval(seasonalityInterval)
      self.java = forecast_builder_java

    def input(self, metric):
        """Adds given metric as an explanatory variable to forecast model.
        
        Arguments:
          metric: object of class metric
        Returns:
          Object of class forecast
        """
        if not metric.__class__.__name__ == 'Metric':
            sys.exit("metric should have class 'Metric'")
        self.java.addIndependentVariable(metric.java)
        return self

    def apply(self):
        """Runs forecasting algorithm on a configured forecast object.
        
        Arguments:
          None
        Returns:
          Object of class forecast
        """        
        util_validate()
        forecast_lazy_metric = Metric(self.java.build())

        return forecast_lazy_metric
