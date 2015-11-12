import os
import json


# add jar to classpacth
os.environ['CLASSPATH'] = "jar/portfolioeffect-quant-client-1.0-allinone.jar"
print 'CLASSPATH: ', os.environ['CLASSPATH']
from jnius import autoclass


#
# Global vars
#

clientConnection = None
clientCredentials = None
