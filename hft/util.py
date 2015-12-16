from __init__ import *


# 
# Utility Methods
# 
def util_setCredentials(username, password, apiKey, host='snowfall04.snowfallsystems.com'):
    # TODO write credentials to file
    global clientCredentials
    clientCredentials = {'username': username, 'password': password, 'apiKey': apiKey, 'host': host }
        

def util_validateConnection():
    # create client connection

    if clientCredentials is None:
        raise ValueError("""Function util_setCredentials() should be called before. \n 
        To retrieve your account credentials, log in to your account or register for a free account at  \n
        https://www.portfolioeffect.com/registration""");

    global clientConnection
    ClientConnection = autoclass('com.portfolioeffect.quant.client.ClientConnection')
    clientConnection = ClientConnection()
    
    # set credentials
    clientConnection.setUsername(clientCredentials.get('username'));
    clientConnection.setPassword(clientCredentials.get('password'));
    clientConnection.setApiKey(clientCredentials.get('apiKey'));
    clientConnection.setHost(clientCredentials.get('host'));
    
    return clientConnection


def util_getResult( data ):
    
    if data.hasError():
        raise ValueError(data.getErrorMessage())
        
    result=[]
    dataNames=data.getDataNames();
    
    for dataName in dataNames:
        dataType = data.getDataType(dataName);
        
        result.append({
          'DOUBLE': lambda : data.getDouble(dataName),
          'DOUBLE_VECTOR': lambda : data.getDoubleArray(dataName),
          'DOUBLE_MATRIX': lambda : data.getDoubleMatrix(dataName),
          'INT_VECTOR': lambda : data.getIntArray(dataName),
          'LONG_VECTOR': lambda : data.getLongArray(dataName),
          'PORTFOLIO': lambda : data.getPortfolio(dataName)
        }[dataType]())
              
    return result

def util_validate():
    # TODO finish implementation
    return

def util_checkErrors():
    #TODO finish implementation
    return

def util_metric(portfolio, args):
    #TODO  finish implementation
    util_validate()
    data = portfolio.getMetric(json.dumps(args))
    return util_getResult(data)

def util_isNumeric(vector):
    return all(item.isdigit() for item in vector)

