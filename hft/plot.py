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

def ascii_encode_dict(data):
    ascii_encode = lambda x: x.encode('ascii') if isinstance(x, unicode) else x 
    return dict(map(ascii_encode, pair) for pair in data.items()) 


def util_timezone(metric):
    etz = pytz.timezone('US/Eastern')
    utc = pytz.timezone('UTC')
    baseTime = dt.datetime(1970, 1, 1, tzinfo=utc)
    times = [etz.normalize(baseTime + dt.timedelta(seconds=ts)) for ts in [float(x) / 1000.0 for x in metric]]
    return times

def util_plot2d(metric, title='', subtitle = '', line_size=2, title_size=17):
    if not isinstance(metric, list):
        sys.exit("metric should have class 'list'")
    if not isinstance(title, str):
        sys.exit("title should have class 'str'")
    if not isinstance(subtitle, str):
        sys.exit("subtitle should have class 'str'")
    times=util_timezone(metric[0])

    def format_date(x, pos=None):
        thisind = np.clip(int(x+0.5), 0, N-1)
        return times[thisind].strftime('%b-%d %H-%M')
    N = len(metric[1])
    ind = np.arange(N)  # the evenly spaced plot indices
    fig, ax = plt.subplots()
    ax.plot(ind, metric[1], lw=line_size)
    ax.xaxis.set_major_formatter(ticker.FuncFormatter(format_date))
    fig.autofmt_xdate()
    
    plt.suptitle(title, y=0.99, fontsize=title_size)
    plt.title(subtitle, fontsize=title_size-5)

    plt.grid(True) 
    plt.show()
           
plotStyle = ascii_encode_dict(json.loads(pkgutil.get_data('hft', 'style.json')))
matplotlib.rcParams.update(plotStyle)
locale.setlocale(locale.LC_ALL, 'C')