import json
import locale
import matplotlib
import pytz
import pkgutil
import datetime as dt
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import sys
import codecs


def ascii_encode_dict(data):
    return dict(ascii_encode( pair) for pair in data.items()) 

def ascii_encode(x):
    if sys.version_info >= (3,0,0):
        # for Python 3
        if isinstance(x, bytes):
            x = x.decode('ascii')
        else:
             x   
    else:
        # for Python 2
        if isinstance(x, unicode): 
            x.encode('ascii')
        else: 
            x
    return x   


def util_timezone(metric):
    etz = pytz.timezone('US/Eastern')
    utc = pytz.timezone('UTC')
    baseTime = dt.datetime(1970, 1, 1, tzinfo=utc)
    times = [etz.normalize(baseTime + dt.timedelta(seconds=ts)) for ts in [float(x) / 1000.0 for x in metric]]
    return times

def util_plot2d(metric, title='', subtitle = '', line_size=2, title_size=17,date_formatter='%b-%d-%y %H-%M',plot_size=(6,6)):
    if not isinstance(metric, list):
        sys.exit("metric should have class 'list'")
    if not isinstance(title, str):
        sys.exit("title should have class 'str'")
    if not isinstance(subtitle, str):
        sys.exit("subtitle should have class 'str'")
    times=util_timezone(metric[0])

    def format_date(x, pos=None):
        thisind = np.clip(int(x+0.5), 0, N-1)
        return times[thisind].strftime(date_formatter)
    N = len(metric[1])
    ind = np.arange(N)  # the evenly spaced plot indices
    fig, ax = plt.subplots()
    ax.plot(ind, metric[1], lw=line_size)
    ax.xaxis.set_major_formatter(ticker.FuncFormatter(format_date))
    fig.autofmt_xdate()

    
    plt.suptitle(title, y=0.99, fontsize=title_size)
    plt.title(subtitle, fontsize=title_size-5)
    plt.rcParams['figure.figsize'] = plot_size

    plt.grid(True) 
    plt.show()

pk=pkgutil.get_data('hft', 'style.json')
lo=json.loads(pk.decode("utf-8"))
plotStyle=ascii_encode_dict(lo)

matplotlib.rcParams.update(plotStyle)
locale.setlocale(locale.LC_ALL, 'C')