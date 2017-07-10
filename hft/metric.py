"""
This module incorporates the notion of "lazy" portfolio or position metric.
"""


from __init__ import *
from plot import *
from util import *


class Metric:
    """Class that incorporates the notion of "lazy" portfolio or position metric."""
    def __repr__(self):
        return self.java.getDescription()
    def __str__(self):
        return self.java.getDescription()
    def plot(self, title='', subtitle = '', line_size=2, title_size=17):
        util_plot2d(compute(self)[0],title=title, subtitle = subtitle, line_size=line_size, title_size=title_size)
    def __init__(self, data,symbol=''):
        if str(type(data))=="<class 'jnius.reflect.com.portfolioeffect.quant.client.result.LazyMetric'>":
            self.java=data
        else:
            metric_autoclass=autoclass("com.portfolioeffect.quant.client.result.SavedMetric")
            list_long_time = util_POSIXTime_to_TLongArrayList(data[0])
            list_double_price = util_to_TArrayList(data[1], 'Double')
            self.java = metric_autoclass(list_double_price,list_long_time)
            self.java.setDescription(symbol)
    def __add__(self, other):
        if isinstance(other, (float, int)):
            simple_lazy_metric_builder_autoclass = autoclass('com.portfolioeffect.quant.client.util.SimpleLazyMetricBuilder')
            simple_lazy_metric_builder = simple_lazy_metric_builder_autoclass()

            simple_lazy_metric_builder=simple_lazy_metric_builder.setMetricName("CONST");
            simple_lazy_metric_builder = simple_lazy_metric_builder.setParam("args", str(other));
            temp=Metric(simple_lazy_metric_builder.build(self.java.getPortfolio()));
        else:
            temp=other;
            print(str(type(temp.java)))
        simple_lazy_metric_builder_autoclass = autoclass('com.portfolioeffect.quant.client.util.SimpleLazyMetricBuilder')
        simple_lazy_metric_builder = simple_lazy_metric_builder_autoclass()
        simple_lazy_metric_builder = simple_lazy_metric_builder.setMetricName("SUM");
        simple_lazy_metric_builder = simple_lazy_metric_builder.addToList("args", self.java);
        simple_lazy_metric_builder = simple_lazy_metric_builder.addToList("args", temp.java);
        build=simple_lazy_metric_builder.build(self.java.getPortfolio())
        result = Metric(build);
        print(str(type(result.java)))
        return result

    def __sub__(self, other):
        if isinstance(other, (float, int)):
            simple_lazy_metric_builder_autoclass = autoclass('com.portfolioeffect.quant.client.util.SimpleLazyMetricBuilder')
            simple_lazy_metric_builder = simple_lazy_metric_builder_autoclass()

            simple_lazy_metric_builder=simple_lazy_metric_builder.setMetricName("CONST");
            simple_lazy_metric_builder = simple_lazy_metric_builder.setParam("args", str(other));
            other=Metric(simple_lazy_metric_builder.build(self.java.getPortfolio()));

        other=other*(-1)
        simple_lazy_metric_builder_autoclass = autoclass('com.portfolioeffect.quant.client.util.SimpleLazyMetricBuilder')
        simple_lazy_metric_builder = simple_lazy_metric_builder_autoclass()
        simple_lazy_metric_builder = simple_lazy_metric_builder.setMetricName("SUM");
        simple_lazy_metric_builder = simple_lazy_metric_builder.addToList("args", self.java);
        simple_lazy_metric_builder = simple_lazy_metric_builder.addToList("args", other.java);
        result = Metric(simple_lazy_metric_builder.build(self.java.getPortfolio()));
        return Metric(result)
    def __mul__(self, other):
        if isinstance(other, (float, int)):
            simple_lazy_metric_builder_autoclass = autoclass('com.portfolioeffect.quant.client.util.SimpleLazyMetricBuilder')
            simple_lazy_metric_builder = simple_lazy_metric_builder_autoclass()

            simple_lazy_metric_builder=simple_lazy_metric_builder.setMetricName("CONST");
            simple_lazy_metric_builder = simple_lazy_metric_builder.setParam("args", str(other));
            other=Metric(simple_lazy_metric_builder.build(self.java.getPortfolio()));

        simple_lazy_metric_builder_autoclass = autoclass('com.portfolioeffect.quant.client.util.SimpleLazyMetricBuilder')
        simple_lazy_metric_builder = simple_lazy_metric_builder_autoclass()
        simple_lazy_metric_builder = simple_lazy_metric_builder.setMetricName("PRODUCT");
        simple_lazy_metric_builder = simple_lazy_metric_builder.addToList("args", self.java);
        simple_lazy_metric_builder = simple_lazy_metric_builder.addToList("args", other.java);
        result = Metric(simple_lazy_metric_builder.build(self.java.getPortfolio()));
        return result

    def __div__(self, other):
        if isinstance(other, (float, int)):
            simple_lazy_metric_builder_autoclass = autoclass('com.portfolioeffect.quant.client.util.SimpleLazyMetricBuilder')
            simple_lazy_metric_builder = simple_lazy_metric_builder_autoclass()

            simple_lazy_metric_builder=simple_lazy_metric_builder.setMetricName("CONST");
            simple_lazy_metric_builder = simple_lazy_metric_builder.setParam("args", str(other));
            other=Metric(simple_lazy_metric_builder.build(self.java.getPortfolio()));

        simple_lazy_metric_builder_autoclass = autoclass('com.portfolioeffect.quant.client.util.SimpleLazyMetricBuilder')
        simple_lazy_metric_builder = simple_lazy_metric_builder_autoclass()
        simple_lazy_metric_builder = simple_lazy_metric_builder.setMetricName("FRACTION");
        simple_lazy_metric_builder = simple_lazy_metric_builder.addToList("args", self.java);
        simple_lazy_metric_builder = simple_lazy_metric_builder.addToList("args", other.java);
        result = Metric(simple_lazy_metric_builder.build(self.java.getPortfolio()));
        return result

    def __radd__(self, other):
        if isinstance(other, (float, int)):
            simple_lazy_metric_builder_autoclass = autoclass('com.portfolioeffect.quant.client.util.SimpleLazyMetricBuilder')
            simple_lazy_metric_builder = simple_lazy_metric_builder_autoclass()

            simple_lazy_metric_builder=simple_lazy_metric_builder.setMetricName("CONST");
            simple_lazy_metric_builder = simple_lazy_metric_builder.setParam("args", str(other));
            other=Metric(simple_lazy_metric_builder.build(self.java.getPortfolio()));

        simple_lazy_metric_builder_autoclass = autoclass('com.portfolioeffect.quant.client.util.SimpleLazyMetricBuilder')
        simple_lazy_metric_builder = simple_lazy_metric_builder_autoclass()
        simple_lazy_metric_builder = simple_lazy_metric_builder.setMetricName("SUM");
        simple_lazy_metric_builder = simple_lazy_metric_builder.addToList("args", self.java);
        simple_lazy_metric_builder = simple_lazy_metric_builder.addToList("args", other.java);
        result = Metric(simple_lazy_metric_builder.build(self.java.getPortfolio()));
        return result
    def __rsub__(self, other):
        if isinstance(other, (float, int)):
            simple_lazy_metric_builder_autoclass = autoclass('com.portfolioeffect.quant.client.util.SimpleLazyMetricBuilder')
            simple_lazy_metric_builder = simple_lazy_metric_builder_autoclass()

            simple_lazy_metric_builder=simple_lazy_metric_builder.setMetricName("CONST");
            simple_lazy_metric_builder = simple_lazy_metric_builder.setParam("args", str(other));
            other=Metric(simple_lazy_metric_builder.build(self.java.getPortfolio()));

        other=other*(-1)
        simple_lazy_metric_builder_autoclass = autoclass('com.portfolioeffect.quant.client.util.SimpleLazyMetricBuilder')
        simple_lazy_metric_builder = simple_lazy_metric_builder_autoclass()
        simple_lazy_metric_builder = simple_lazy_metric_builder.setMetricName("SUM");
        simple_lazy_metric_builder = simple_lazy_metric_builder.addToList("args", self.java);
        simple_lazy_metric_builder = simple_lazy_metric_builder.addToList("args", other.java);
        result = Metric(simple_lazy_metric_builder.build(self.java.getPortfolio()));
        return result
    def __rmul__(self, other):
        if isinstance(other, (float, int)):
            simple_lazy_metric_builder_autoclass = autoclass('com.portfolioeffect.quant.client.util.SimpleLazyMetricBuilder')
            simple_lazy_metric_builder = simple_lazy_metric_builder_autoclass()

            simple_lazy_metric_builder=simple_lazy_metric_builder.setMetricName("CONST");
            simple_lazy_metric_builder = simple_lazy_metric_builder.setParam("args", str(other));
            other=Metric(simple_lazy_metric_builder.build(self.java.getPortfolio()));

        simple_lazy_metric_builder_autoclass = autoclass('com.portfolioeffect.quant.client.util.SimpleLazyMetricBuilder')
        simple_lazy_metric_builder = simple_lazy_metric_builder_autoclass()
        simple_lazy_metric_builder = simple_lazy_metric_builder.setMetricName("PRODUCT");
        simple_lazy_metric_builder = simple_lazy_metric_builder.addToList("args", self.java);
        simple_lazy_metric_builder = simple_lazy_metric_builder.addToList("args", other.java);
        result = Metric(simple_lazy_metric_builder.build(self.java.getPortfolio()));
        return result
    def __rdiv__(self, other):
        if isinstance(other, (float, int)):
            simple_lazy_metric_builder_autoclass = autoclass('com.portfolioeffect.quant.client.util.SimpleLazyMetricBuilder')
            simple_lazy_metric_builder = simple_lazy_metric_builder_autoclass()

            simple_lazy_metric_builder=simple_lazy_metric_builder.setMetricName("CONST");
            simple_lazy_metric_builder = simple_lazy_metric_builder.setParam("args", str(other));
            other=Metric(simple_lazy_metric_builder.build(self.java.getPortfolio()));

        simple_lazy_metric_builder_autoclass = autoclass('com.portfolioeffect.quant.client.util.SimpleLazyMetricBuilder')
        simple_lazy_metric_builder = simple_lazy_metric_builder_autoclass()
        simple_lazy_metric_builder = simple_lazy_metric_builder.setMetricName("FRACTION");
        simple_lazy_metric_builder = simple_lazy_metric_builder.addToList("args", self.java);
        simple_lazy_metric_builder = simple_lazy_metric_builder.addToList("args", other.java);
        result = Metric(simple_lazy_metric_builder.build(self.java.getPortfolio()));
        return result
    def sqrt(self):
        simple_lazy_metric_builder_autoclass = autoclass('com.portfolioeffect.quant.client.util.SimpleLazyMetricBuilder')
        simple_lazy_metric_builder = simple_lazy_metric_builder_autoclass()
        simple_lazy_metric_builder = simple_lazy_metric_builder.setMetricName("SQRT");
        simple_lazy_metric_builder = simple_lazy_metric_builder.addToList("args", self.java);
        result = Metric(simple_lazy_metric_builder.build(self.java.getPortfolio()));
        return result



def util_metric(asset, args):
    util_validate()
    lazy_metric_builder_autoclass = autoclass('com.portfolioeffect.quant.client.util.LazyMetricBuilder')
    lazy_metric_builder = lazy_metric_builder_autoclass(json.dumps(args))
    lazy_metric = lazy_metric_builder.build(asset.java)
    metric=Metric(lazy_metric)
    return metric


def compute(*args):
    """Metric object is not evaluated until compute() method is called on it. Method would display calculation progress and would use Metric object's disk cache to store any computational results obtained in the process.
        
    Arguments:
        ...one or multiple objects of class Metric.
    Returns:
        one or multiple objects of class Metric.
    """    
    util_validate()
    metrics=[]
    for arg in args:
        metrics.append(util_getResult(arg.java,True));
    return metrics


def util_plot(*args, **kwargs):
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

    if 'legend' in plot_keys:
        legend = kwargs['legend']
    else:
        legend = 1

    if 'date_formatter' in plot_keys:
        date_formatter = kwargs['date_formatter']
    else:
        date_formatter = '%b-%d-%y %H-%M'

    if 'plot_size' in plot_keys:
        plot_size = kwargs['title_size']
    else:
        plot_size = (6, 6)

    def format_date(x, pos=None):
        thisind = np.clip(int(x + 0.5), 0, N - 1)
        return times[thisind].strftime(date_formatter)

    fig, ax = plt.subplots(facecolor='white')

    metric_synchronizer_autoclass = autoclass('com.portfolioeffect.quant.client.util.MetricSynchronizer')
    metric_synchronizer = metric_synchronizer_autoclass()

    for i in range(len(args)):
        metric_synchronizer.add(args[i].java)
    time_list = util_TLongArrayList_to_time(metric_synchronizer.getTimeList())
    times = util_timezone(time_list)
    N = len(times)
    for i in range(len(args)):
        label = args[i] if legend == 1 else legend[i]
        ax.plot(range(N), metric_synchronizer.getValue(int(i)), lw=line_size, label=label)
    ax.xaxis.set_major_formatter(ticker.FuncFormatter(format_date))
    ax.set_axis_bgcolor('white')
    fig.autofmt_xdate()

    plt.suptitle(title, y=0.99, fontsize=title_size)
    plt.title(subtitle, fontsize=title_size - 5)
    legend = plt.legend()
    frame = legend.get_frame()
    frame.set_facecolor('white')
    plt.rcParams['figure.figsize'] = plot_size
    plt.grid(True)
    plt.show()
    