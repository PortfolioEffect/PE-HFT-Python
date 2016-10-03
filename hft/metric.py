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
    def __init__(self, data):
        if str(type(data))=="<class 'jnius.reflect.com.portfolioeffect.quant.client.result.LazyMetric'>":
            self.java=data
        else:
            metric_autoclass=autoclass("com.portfolioeffect.quant.client.result.SavedMetric")
            list_long_time = util_POSIXTime_to_TLongArrayList(data[0])
            list_double_price = util_to_TArrayList(data[1], 'Double')
            self.java = metric_autoclass(list_double_price,list_long_time)


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

def util_plot(*args,**kwargs):
    util_validate()
    plot_keys=kwargs.keys()

    if 'title' in plot_keys:
        title=kwargs['title']
    else:
        title=""

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

    def format_date(x, pos=None):
        thisind = np.clip(int(x + 0.5), 0, N - 1)
        return times[thisind].strftime('%b-%d %H-%M')
    fig, ax = plt.subplots()

    metric_synchronizer_autoclass = autoclass('com.portfolioeffect.quant.client.util.MetricSynchronizer')
    metric_synchronizer = metric_synchronizer_autoclass()

    for i in range(len(args)):
        metric_synchronizer.add(args[i].java)
    time_list = util_TLongArrayList_to_time(metric_synchronizer.getTimeList())
    times = util_timezone(time_list)
    N = len(times)
    for i in range(len(args)):
        label = args[i] if legend == 1 else legend[i]
        ax.plot(range(N), metric_synchronizer.getValue(int(i)), lw=line_size,label=label)
    ax.xaxis.set_major_formatter(ticker.FuncFormatter(format_date))
    fig.autofmt_xdate()

    plt.suptitle(title, y=0.99, fontsize=title_size)
    plt.title(subtitle, fontsize=title_size-5)
    plt.legend()

    plt.grid(True)
    plt.show()