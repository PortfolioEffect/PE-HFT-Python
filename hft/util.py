from __init__ import *


# 
# Utility Methods
#


def util_setCredentials(username, password, apiKey, host='quant07.portfolioeffect.com'):
    # TODO write credentials to file
    global CLIENT_CONNECTION
    CLIENT_CONNECTION = {'username': username, 'password': password, 'apiKey': apiKey, 'host': host }


def util_validateConnection():
    # create client connection
    global CLIENT_CONNECTION
    if CLIENT_CONNECTION is None:
        raise ValueError("""Function util_setCredentials() should be called before. \n
        To retrieve your account credentials, log in to your account or register for a free account at  \n
        https://www.portfolioeffect.com/registration""");

    ClientConnection = autoclass('com.portfolioeffect.quant.client.ClientConnection')
    client_connection = ClientConnection()

    # set credentials
    client_connection.setUsername(CLIENT_CONNECTION.get('username'));
    client_connection.setPassword(CLIENT_CONNECTION.get('password'));
    client_connection.setApiKey(CLIENT_CONNECTION.get('apiKey'));
    client_connection.setHost(CLIENT_CONNECTION.get('host'));
    
    return client_connection

def util_POSIXTime_to_TLongArrayList(data):
    TIntArrayList_autoclass = autoclass("gnu.trove.list.array.TIntArrayList")
    hours = [int(x / (60 * 60 * 1000)) for x in data]
    millisec_from_hour_start = [int(y - x * 60 * 60 * 1000) for x, y in zip(hours, data)]
    list_int_hours = TIntArrayList_autoclass()
    list_int_millisec_from_hour_start = TIntArrayList_autoclass()
    for i in range(len(hours)):
        list_int_hours.add(hours[i])
        list_int_millisec_from_hour_start.add(millisec_from_hour_start[i])
    lazy_metric_autoclass = autoclass('com.portfolioeffect.quant.client.result.LazyMetric')
    lazy_metric = lazy_metric_autoclass("1")
    list_long_time = lazy_metric.toTLongArrayList(list_int_hours, list_int_millisec_from_hour_start)
    return list_long_time

def util_to_TArrayList(data,type):
    TArrayList_autoclass={'Double': lambda: autoclass("gnu.trove.list.array.TDoubleArrayList"),
        'Int': lambda: autoclass("gnu.trove.list.array.TIntArrayList"),
        'Float': lambda: autoclass("gnu.trove.list.array.TFloatArrayList")}[type]()
    list = TArrayList_autoclass()
    for i in range(len(data)):
        list.add(data[i])
    return list

def util_TLongArrayList_to_time(TLongArrayList):
    util_autoclass=autoclass('com.portfolioeffect.quant.client.util.Util')
    util=util_autoclass()
    hours=util.getHours(TLongArrayList).toArray()
    millisec_from_hour_start = util.getMillisecFromHourStart(TLongArrayList).toArray()
    time = [x * 60 * 60 * 1000 + y for x, y in zip(hours, millisec_from_hour_start)]
    return time

def util_getResult( data,metricClass=False ):
    util_checkErrors(data)

    result=[]
    if metricClass:
        hours=data.getIntArray("hours")
        millisec_from_hour_start=data.getIntArray("millisec_from_hour_start")
        time=[x*60*60*1000 + y for x, y in zip(hours, millisec_from_hour_start)]
        value=data.getDoubleArray('value')
        result.append(time)
        result.append(value)
    else:
        dataNames=data.getDataNames()
    
        for dataName in dataNames:
          dataType = data.getDataType(dataName)
          result.append({
           'DOUBLE': lambda : data.getDouble(dataName),
           'DOUBLE_VECTOR': lambda : data.getDoubleArray(dataName),
           'DOUBLE_MATRIX': lambda : data.getDoubleMatrix(dataName),
           'INT_VECTOR': lambda : data.getIntArray(dataName),
           'LONG_VECTOR': lambda : data.getLongArray(dataName),
           'STRING_VECTOR': lambda : data.getStringArray(dataName),
           'PORTFOLIO': lambda : data.getPortfolio(dataName)
          }[dataType]())
              
    return result

def util_validate():
    global CLIENT_CONNECTION
    if CLIENT_CONNECTION is None:
        raise ValueError("""Function util_setCredentials() should be called before. \n
        To retrieve your account credentials, log in to your account or register for a free account at  \n
        https://www.portfolioeffect.com/registration""");

    ClientConnection = autoclass('com.portfolioeffect.quant.client.ClientConnection')
    client_connection = ClientConnection()

    # set credentials
    client_connection.setUsername(CLIENT_CONNECTION.get('username'));
    client_connection.setPassword(CLIENT_CONNECTION.get('password'));
    client_connection.setApiKey(CLIENT_CONNECTION.get('apiKey'));
    client_connection.setHost(CLIENT_CONNECTION.get('host'));
    return None

def util_checkErrors(data):
    #TODO finish implementation
    if (data.hasError()):
      message=data.getErrorMessage()
      print message


    return

def util_print_table(lines, separate_head=True):
    """Prints a formatted table given a 2 dimensional array"""
    # Count the column width
    widths = []
    for line in lines:
        for i, size in enumerate([len(x) for x in line]):
            while i >= len(widths):
                widths.append(0)
            if size > widths[i]:
                widths[i] = size

    # Generate the format string to pad the columns
    print_string = ""
    for i, width in enumerate(widths):
        print_string += "{" + str(i) + ":" + str(width) + "} | "
    if (len(print_string) == 0):
        return
    print_string = print_string[:-3]

    # Print the actual data
    for i, line in enumerate(lines):
        print(print_string.format(*line))
        if (i == 0 and separate_head):
            print("-" * (sum(widths) + 3 * (len(widths) - 1)))
