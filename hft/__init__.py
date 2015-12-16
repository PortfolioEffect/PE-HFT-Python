import json
import os


# add jar to classpacth
os.environ['CLASSPATH'] = os.path.join(os.path.dirname(__file__), 'jar/portfolioeffect-quant-client-1.0-allinone.jar')
#print 'CLASSPATH: ', os.environ['CLASSPATH']

from jnius import autoclass

#
# Global vars
#

clientConnection = None
clientCredentials = None
