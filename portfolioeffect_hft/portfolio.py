"""
Assuming this is file mymodule.py, then this string, being the
first statement in the file, will become the "mymodule" module's
docstring when the file is imported.
"""

from __init__ import *
from util import * 

# 
# Portfolio Methods
#

def portfolio_create(fromTime, toTime, index = 'SPY'):
    
    # TODO add user data
    
    global clientConnection  
    if clientConnection is None:
        clientConnection = util_validateConnection()
   
    Portfolio = autoclass('com.portfolioeffect.quant.client.portfolio.Portfolio')
    portfolio = Portfolio(clientConnection)
    
    result = portfolio.setFromTime(fromTime);
    if result.hasError():
         raise ValueError(result.getErrorMessage());

    result = portfolio.setToTime(toTime);
    if result.hasError():
        raise ValueError(result.getErrorMessage());
    
    result = portfolio.addIndex(index);
    if result.hasError():
        raise ValueError(result.getErrorMessage());
    
    return portfolio


def portfolio_symbols(portfolio):
    util_validate()
    result = portfolio.getSymbols()  
    return result

# TODO add vector version
# simple method to add positions   
def portfolio_addPosition(portfolio, symbol, quantity):
    result = portfolio.addPosition(symbol,quantity); 
    if result.hasError():
        raise ValueError(result.getErrorMessage());
   
def portfolio_startBatch(portfolio):
    portfolio.startBatch()

def portfolio_endBatch(portfolio):
    result=portfolio.finishBatch()
    util_checkErrors(result)
   
def portfolio_removePosition (portfolio,symbol):
    
    """Sample function description.

    Args:
        param1: The first parameter.
        param2: The second parameter.

    Returns:
        True if successful, False otherwise.

    """
    
    portfolio.removePositionQuantity(symbol)
    portfolio.removePositionPrice(symbol)
    
    
def portfolio_value(portfolio):
    return util_metric(portfolio, {'metric':'PORTFOLIO_VALUE'})  

def portfolio_return(portfolio):
    return util_metric(portfolio, {'metric':'PORTFOLIO_RETURN'})  

def portfolio_expectedReturn(portfolio):
    return util_metric(portfolio, {'metric':'PORTFOLIO_EXPECTED_RETURN'})  

def portfolio_profit(portfolio):
    return util_metric(portfolio, {'metric':'PORTFOLIO_PROFIT'})  

def portfolio_beta(portfolio):
    return util_metric(portfolio, {'metric':'PORTFOLIO_BETA'})  

def portfolio_alpha(portfolio):
    return util_metric(portfolio, {'metric':'PORTFOLIO_ALPHA'})  

def portfolio_variance(portfolio):
    return util_metric(portfolio, {'metric':'PORTFOLIO_VARIANCE'})  

def portfolio_maxDrawdown(portfolio):
    return util_metric(portfolio, {'metric':'PORTFOLIO_MAX_DRAWDOWN'})  

def portfolio_calmarRatio(portfolio):
    return util_metric(portfolio, {'metric':'PORTFOLIO_CALMAR_RATIO'})  

def portfolio_VaR(portfolio,confidenceInterval=0.95):
    return util_metric(portfolio, {'metric':'PORTFOLIO_VAR','confidenceInterval':confidenceInterval})  

def portfolio_CVaR(portfolio,confidenceInterval=0.95):
    return util_metric(portfolio, {'metric':'PORTFOLIO_CVAR','confidenceInterval':confidenceInterval})  
 
def portfolio_modifiedSharpeRatio(portfolio,confidenceInterval=0.95):
    return util_metric(portfolio, {'metric':'PORTFOLIO_SHARPE_RATIO_MOD','confidenceInterval':confidenceInterval})  
 
def portfolio_starrRatio(portfolio,confidenceInterval=0.95):
    return util_metric(portfolio, {'metric':'PORTFOLIO_STARR_RATIO','confidenceInterval':confidenceInterval})  
 
def portfolio_sharpeRatio(portfolio):
    return util_metric(portfolio, {'metric':'PORTFOLIO_SHARPE_RATIO'})  

def portfolio_treynorRatio(portfolio):
    return util_metric(portfolio, {'metric':'PORTFOLIO_TREYNOR_RATIO'})  

def portfolio_skewness(portfolio):
    return util_metric(portfolio, {'metric':'PORTFOLIO_SKEWNESS'})  

def portfolio_kurtosis(portfolio):
    return util_metric(portfolio, {'metric':'PORTFOLIO_KURTOSIS'})  

def portfolio_informationRatio(portfolio):
    return util_metric(portfolio, {'metric':'PORTFOLIO_INFORMATION_RATIO'})  

def portfolio_jensensAlpha(portfolio):
    return util_metric(portfolio, {'metric':'PORTFOLIO_ALPHA_JENSEN'})  

def portfolio_omegaRatio(portfolio,thresholdReturn):
    return util_metric(portfolio, {'metric':'PORTFOLIO_OMEGA_RATIO','thresholdReturn':thresholdReturn})  

def portfolio_rachevRatio(portfolio,confidenceIntervalA=0.95,confidenceIntervalB=0.95):
     return util_metric(portfolio, {'metric':'PORTFOLIO_RACHEV_RATIO','confidenceIntervalAlpha':confidenceIntervalA,'confidenceIntervalBeta':confidenceIntervalB})  
    
def portfolio_gainVariance(portfolio):
    return util_metric(portfolio, {'metric':'PORTFOLIO_GAIN_VARIANCE'})  

def portfolio_lossVariance(portfolio):
    return util_metric(portfolio, {'metric':'PORTFOLIO_LOSS_VARIANCE'})  

def portfolio_downsideVariance(portfolio,thresholdReturn):
    return util_metric(portfolio, {'metric':'PORTFOLIO_DOWNSIDE_VARIANCE','thresholdReturn':thresholdReturn})   

def portfolio_upsideVariance(portfolio,thresholdReturn):
    return util_metric(portfolio, {'metric':'PORTFOLIO_UPSIDE_VARIANCE','thresholdReturn':thresholdReturn})   
    
def portfolio_expectedDownsideReturn(portfolio,thresholdReturn):
    return util_metric(portfolio, {'metric':'PORTFOLIO_EXPECTED_DOWNSIDE_THRESHOLD_RETURN','thresholdReturn':thresholdReturn})   
    
def portfolio_expectedUpsideReturn(portfolio,thresholdReturn):
    return util_metric(portfolio, {'metric':'PORTFOLIO_EXPECTED_UPSIDE_THRESHOLD_RETURN','thresholdReturn':thresholdReturn})   

def portfolio_hurstExponent(portfolio):
    return util_metric(portfolio, {'metric':'PORTFOLIO_HURST_EXPONENT'})   
    
def portfolio_fractalDimension(portfolio):
    return util_metric(portfolio, {'metric':'PORTFOLIO_FRACTAL_DIMENSION'})   

def portfolio_txnCosts(portfolio):
    return util_metric(portfolio, {'metric':'PORTFOLIO_TRANSACTION_COSTS_SIZE'}) 

def portfolio_sortinoRatio(portfolio,thresholdReturn):
    return util_metric(portfolio, {'metric':'PORTFOLIO_SORTINO_RATIO','thresholdReturn':thresholdReturn})   

def portfolio_upsideDownsideVarianceRatio(portfolio,thresholdReturn):
    return util_metric(portfolio, {'metric':'PORTFOLIO_UPSIDE_DOWNSIDE_VARIANCE_RATIO','thresholdReturn':thresholdReturn})   

def portfolio_gainLossVarianceRatio(portfolio):
    return util_metric(portfolio, {'metric':'PORTFOLIO_GAIN_LOSS_VARIANCE_RATIO'})  

def portfolio_downCaptureRatio(portfolio):
    return util_metric(portfolio, {'metric':'PORTFOLIO_DOWN_CAPTURE_RATIO'})  

def portfolio_upCaptureRatio(portfolio):
    return util_metric(portfolio, {'metric':'PORTFOLIO_UP_CAPTURE_RATIO'})  
    
def portfolio_downNumberRatio(portfolio):
    return util_metric(portfolio, {'metric':'PORTFOLIO_DOWN_NUMBER_RATIO'})  

def portfolio_upNumberRatio(portfolio):
    return util_metric(portfolio, {'metric':'PORTFOLIO_UP_NUMBER_RATIO'})  
    
def portfolio_downPercentageRatio(portfolio):
    return util_metric(portfolio, {'metric':'PORTFOLIO_DOWN_PERCENTAGE_RATIO'})  
    
def portfolio_upPercentageRatio(portfolio):
    return util_metric(portfolio, {'metric':'PORTFOLIO_UP_PERCENTAGE_RATIO'})  

# portfolio_moment(portfolio,order){
#     if(order=="all"){
#         order=c(3,4)
#     }
#     totalResult<-NULL
#     for(i in order){
#         result<-util_metric(argList=as.list(environment()),portfolio=portfolio,metric=paste("PORTFOLIO_MOMENT",i,sep=""))
#         if(is.null(totalResult)){
#             totalResult<-result
#         }else{
#             totalResult=cbind(totalResult,result[,2])
#         }
#     }
#     return(totalResult)}
# 
# portfolio_cumulant(portfolio,order){
#     if(order=="all"){
#         order=c(3,4)
#     }
#     totalResult<-NULL
#     for(i in order){
#         result<-util_metric(argList=as.list(environment()),portfolio=portfolio,metric=paste("PORTFOLIO_CUMULANT",i,sep=""))
#         if(is.null(totalResult)){
#             totalResult<-result
#         }else{
#             totalResult=cbind(totalResult,result[,2])
#         }
#     }
#     return(totalResult)}
     
# portfolio_pdf<-function(portfolio,pValueLeft,pValueRight,nPoints,addNormalDensity=FALSE){
#     
#     portfolioTemp=portfolio_create(portfolio)
#     set<-portfolio_getSettings(portfolioTemp)
#     .jcall(portfolioTemp@java,returnSig="V", method="setSamplingInterval","last")
#         
#     z<-.jcall(portfolioTemp@java, returnSig="Lcom/portfolioeffect/quant/client/result/MethodResult;",method="getPDF",
#             as.double(pValueLeft),as.double(pValueRight),as.integer(nPoints))
#     
#     result<-list(pdf=.jcall(z,returnSig="[[D",method="getDoubleMatrix", "pdf" ,simplify=TRUE),
#             value=.jcall(z,returnSig="[[D",method="getDoubleMatrix", "x", simplify=TRUE),
#             time=.jcall(z,returnSig="[J",method="getLongArray", "time"))
#     
#     if(addNormalDensity){
#         GaussianMoments=FALSE
#         if(set$densityModel!="NORMAL"){
#             GaussianMoments<-TRUE
#             portfolio_settings(portfolioTemp,densityModel="NORMAL")
#         }
#         z<-.jcall(portfolioTemp@java,
#                 returnSig="Lcom/portfolioeffect/quant/client/result/MethodResult;",method="getPDF",
#                 as.double(pValueLeft),as.double(pValueRight),as.integer(nPoints))
#         
#         result$pdfNormal=.jcall(z,returnSig="[[D",method="getDoubleMatrix", "pdf", simplify=TRUE)
#         result$valueNormal=.jcall(z,returnSig="[[D",method="getDoubleMatrix", "x", simplify=TRUE)
#     }
#     return(result)
# }   

# 
# Position Methods
#

def position_setQuantity(portfolio,symbol,quantity):
    util_validate()
    result = portfolio.setPositionQuantity(symbol, quantity)  
    util_checkErrors(result)

def position_quantity(portfolio,symbol):
    util_validate()
    result = portfolio.getPositionQuantity(symbol)  
    return util_getResult(result)
      
def position_price(portfolio,symbol):
     return util_metric(portfolio, {'metric':'POSITION_PRICE','position': symbol})

def position_profit(portfolio,symbol):
     return util_metric(portfolio, {'metric':'POSITION_PROFIT','position': symbol})
 
def position_return(portfolio,symbol):
    return util_metric(portfolio, {'metric':'POSITION_RETURN','position': symbol})  

def position_expectedReturn(portfolio,symbol):
    return util_metric(portfolio, {'metric':'POSITION_EXPECTED_RETURN','position': symbol})  
 
def position_variance(portfolio, symbol):
    return util_metric(portfolio, {'metric':'POSITION_VARIANCE','position': symbol})
   
def position_maxDrawdown(portfolio,symbol):
    return util_metric(portfolio, {'metric':'POSITION_MAX_DRAWDOWN','position': symbol})
   
def position_calmarRatio(portfolio,symbol):
    return util_metric(portfolio, {'metric':'POSITION_CALMAR_RATIO','position': symbol})
    
def position_weight(portfolio,symbol):
    return util_metric(portfolio, {'metric':'POSITION_WEIGHT','position': symbol})  

def position_value(portfolio,symbol):
    return util_metric(portfolio, {'metric':'POSITION_VALUE','position': symbol})  
   
def position_beta(portfolio,symbol):
    return util_metric(portfolio, {'metric':'POSITION_BETA','position': symbol})  
   
def position_alpha(portfolio,symbol):
    return util_metric(portfolio, {'metric':'POSITION_ALPHA','position': symbol})  
 
def position_returnAutocovariance(portfolio,symbol,lag=10):
    return util_metric(portfolio, {'metric':'POSITION_RETURN_AUTOCOVARIANCE','position': symbol,'lag':lag})  

def position_CVaR(portfolio,symbol,confidenceInterval=0.95):
    return util_metric(portfolio, {'metric':'POSITION_CVAR','position': symbol,'confidenceInterval': confidenceInterval})  

def position_VaR(portfolio,symbol,confidenceInterval=0.95):
    return util_metric(portfolio, {'metric':'POSITION_VAR','position': symbol,'confidenceInterval': confidenceInterval})  

def position_modifiedSharpeRatio(portfolio,symbol,confidenceInterval=0.95):
    return util_metric(portfolio, {'metric':'POSITION_SHARPE_RATIO_MOD','position': symbol,'confidenceInterval': confidenceInterval})  

def position_starrRatio(portfolio,symbol,confidenceInterval=0.95):
    return util_metric(portfolio, {'metric':'POSITION_STARR_RATIO','position': symbol,'confidenceInterval': confidenceInterval})  

def position_sharpeRatio(portfolio,symbol):
    return util_metric(portfolio, {'metric':'POSITION_SHARPE_RATIO','position': symbol})  

def position_treynorRatio(portfolio,symbol):
    return util_metric(portfolio, {'metric':'POSITION_TREYNOR_RATIO','position': symbol})  

def position_skewness(portfolio,symbol):
    return util_metric(portfolio, {'metric':'POSITION_SKEWNESS','position': symbol})  

def position_kurtosis(portfolio,symbol):
    return util_metric(portfolio, {'metric':'POSITION_KURTOSIS','position': symbol})  

def position_informationRatio(portfolio,symbol):
    return util_metric(portfolio, {'metric':'POSITION_INFORMATION_RATIO','position': symbol})  

def position_jensensAlpha(portfolio,symbol):
    return util_metric(portfolio, {'metric':'POSITION_ALPHA_JENSEN','position': symbol})  

def position_covariance(portfolio,symbol1,symbol2):
    return util_metric(portfolio, {'metric':'POSITION_COVARIANCE','positionA': symbol1,'positionB':symbol2})  

def position_correlation(portfolio,symbol1,symbol2):
    return util_metric(portfolio, {'metric':'POSITION_CORRELATION','positionA': symbol1,'positionB':symbol2})  

def position_omegaRatio(portfolio,symbol,thresholdReturn):
    return util_metric(portfolio, {'metric':'POSITION_OMEGA_RATIO','position': symbol,'thresholdReturn':thresholdReturn})  

def position_starrRatio(portfolio,symbol,confidenceIntervalA=0.95,confidenceIntervalB=0.95):
    return util_metric(portfolio, {'metric':'POSITION_RACHEV_RATIO','position': symbol,'confidenceIntervalAlpha': confidenceIntervalAlpha,'confidenceIntervalBeta': confidenceIntervalBeta})  

def position_gainVariance(portfolio,symbol):
    return util_metric(portfolio, {'metric':'POSITION_GAIN_VARIANCE','position': symbol})  

def position_lossVariance(portfolio,symbol):
    return util_metric(portfolio, {'metric':'POSITION_LOSS_VARIANCE','position': symbol})  

def position_downsideVariance(portfolio,symbol,thresholdReturn):
    return util_metric(portfolio, {'metric':'POSITION_DOWNSIDE_VARIANCE','position': symbol,'thresholdReturn':thresholdReturn})  

def position_upsideVariance(portfolio,symbol,thresholdReturn):
    return util_metric(portfolio, {'metric':'POSITION_UPSIDE_VARIANCE','position': symbol,'thresholdReturn':thresholdReturn})  

def position_expectedDownsideReturn(portfolio,symbol,thresholdReturn):
    return util_metric(portfolio, {'metric':'POSITION_EXPECTED_DOWNSIDE_THRESHOLD_RETURN','position': symbol,'thresholdReturn':thresholdReturn})  

def position_expectedUpsideReturn(portfolio,symbol,thresholdReturn):
    return util_metric(portfolio, {'metric':'POSITION_EXPECTED_UPSIDE_THRESHOLD_RETURN','position': symbol,'thresholdReturn':thresholdReturn})  

def position_sortinoRatio(portfolio,symbol,thresholdReturn):
    return util_metric(portfolio, {'metric':'POSITION_SORTINO_RATIO','position': symbol,'thresholdReturn':thresholdReturn})  

def position_upsideDownsideVarianceRatio(portfolio,symbol,thresholdReturn):
    return util_metric(portfolio, {'metric':'POSITION_UPSIDE_DOWNSIDE_VARIANCE_RATIO','position': symbol,'thresholdReturn':thresholdReturn})  

def position_gainLossVarianceRatio(portfolio,symbol):
    return util_metric(portfolio, {'metric':'POSITION_GAIN_LOSS_VARIANCE_RATIO','position': symbol})  

def position_downCaptureRatio(portfolio,symbol):
    return util_metric(portfolio, {'metric':'POSITION_DOWN_CAPTURE_RATIO','position': symbol})  

def position_upCaptureRatio(portfolio,symbol):
    return util_metric(portfolio, {'metric':'POSITION_UP_CAPTURE_RATIO','position': symbol})  

def position_downNumberRatio(portfolio,symbol):
    return util_metric(portfolio, {'metric':'POSITION_DOWN_NUMBER_RATIO','position': symbol})  

def position_upNumberRatio(portfolio,symbol):
    return util_metric(portfolio, {'metric':'POSITION_UP_NUMBER_RATIO','position': symbol})  

def position_downPercentageRatio(portfolio,symbol):
    return util_metric(portfolio, {'metric':'POSITION_DOWN_PERCENTAGE_RATIO','position': symbol})  

def position_upPercentageRatio(portfolio,symbol):
    return util_metric(portfolio, {'metric':'POSITION_UP_PERCENTAGE_RATIO','position': symbol})  

def position_hurstExponent(portfolio,symbol):
    return util_metric(portfolio, {'metric':'POSITION_HURST_EXPONENT','position': symbol})  

def position_fractalDimension(portfolio,symbol):
    return util_metric(portfolio, {'metric':'POSITION_FRACTAL_DIMENSION','position': symbol})  

def position_txnCosts(portfolio,symbol):
    return util_metric(portfolio, {'metric':'POSITION_TRANSACTION_COSTS_SIZE','position': symbol})  



# 
# position_moment(portfolio,symbol,order){
#     util_validate()
#     if(order=="all"){
#         order=c(3,4)
#     }
#     totalResult<-NULL
#     for(i in order){
#         result<-util_metric(argList=as.list(environment()),portfolio=portfolio,position=symbol,metric=paste('POSITION_MOMENT',i,sep=""))
#         if(is.null(totalResult)){
#             totalResult<-result
#         }else{
#             totalResult=cbind(totalResult,result[,2])
#         }
#     }
#     return(totalResult)}
# 
# 
# position_cumulant(portfolio,symbol,order){
#     util_validate()
#     if(order=="all"){
#         order=c(3,4)
#     }
#     totalResult<-NULL
#     for(i in order){
#         result<-util_metric(argList=as.list(environment()),portfolio=portfolio,position=symbol,metric=paste('POSITION_CUMULANT',i,sep=""))
#         if(is.null(totalResult)){
#             totalResult<-result
#         }else{
#             totalResult=cbind(totalResult,result[,2])
#         }
#     }
#     return(totalResult)}
# 
# 
# position_covarianceMatrix(portfolio){
#     util_validate()
#     portfolioTemp=portfolio_create(portfolio)
#     symbols<-portfolio_symbols(portfolioTemp)
#     
#     .jcall(portfolioTemp@java,returnSig="V", method="setSamplingInterval","last")
#         
#     n<-length(symbols)
#     resultMatrix<-matrix(1,nrow=n,ncol=n)
#     .jcall(portfolioTemp@java,returnSig="V", method="createCallGroup",as.integer(n+((n*n-n)/2)))
#     for(i in 2:n){
#         for(j in 1:(i-1)){
#             resultMatrix[i,j]<-util_metric(argList=as.list(environment()),portfolio=portfolioTemp,metric='POSITION_COVARIANCE',positionA=symbols[i],positionB=symbols[j])[2]
#             resultMatrix[j,i]<-resultMatrix[i,j]
#         }
#     }
#     for(i in 1:n){
# 
#         resultMatrix[i,i]<-util_metric(argList=as.list(environment()),portfolio=portfolioTemp,position=symbols[i],metric='POSITION_VARIANCE')[2]
#     }
#     dimnames(resultMatrix) = list(symbols,symbols)
#     return(resultMatrix)
# }
# 
# position_correlationMatrix(portfolio){
#     util_validate()
#     symbols<-portfolio_symbols(portfolio)
#     n<-length(symbols)
#     
#     portfolioTemp=portfolio_create(portfolio)
#     .jcall(portfolioTemp@java,returnSig="V", method="setSamplingInterval","last")
#         
#     resultMatrix<-matrix(1,nrow=n,ncol=n)
#     .jcall(portfolioTemp@java,returnSig="V", method="createCallGroup",as.integer(((n*n-n)/2)))
#     for(i in 2:n){
#         for(j in 1:(i-1)){
#             resultMatrix[i,j]<-util_metric(argList=as.list(environment()),portfolio=portfolioTemp,metric='POSITION_CORRELATION',positionA=symbols[i],positionB=symbols[j])[2]
#             resultMatrix[j,i]<-resultMatrix[i,j]
#         }
#     }
#     dimnames(resultMatrix) = list(symbols,symbols)
#     return(resultMatrix)
# }
# position_pdf<-function(portfolio,symbol,pValueLeft,pValueRight,nPoints,addNormalDensity=FALSE){
#     
#     portfolioTemp=portfolio_create(portfolio)
#     set<-portfolio_getSettings(portfolioTemp)
#     .jcall(portfolioTemp@java,returnSig="V", method="setSamplingInterval","last")
#     
#     z<-.jcall(portfolioTemp@java,
#             returnSig="Lcom/portfolioeffect/quant/client/result/MethodResult;",method="getPDF",
#             as.double(pValueLeft),as.double(pValueRight),as.integer(nPoints), symbol)
#     
#     result<-list(pdf=.jcall(z,returnSig="[[D",method="getDoubleMatrix", "pdf", simplify=TRUE),
#             value=.jcall(z,returnSig="[[D",method="getDoubleMatrix", "x", simplify=TRUE),
#             time=.jcall(z,returnSig="[J",method="getLongArray", "time"))
#     
#     if(addNormalDensity){
#         GaussianMoments=FALSE
#         if(set$densityModel!="NORMAL"){
#             GaussianMoments<-TRUE
#             portfolio_settings(portfolioTemp,densityModel="NORMAL")
#         }
#         z<-.jcall(portfolioTemp@java,
#                 returnSig="Lcom/portfolioeffect/quant/client/result/MethodResult;",method="getPDF",
#                 as.double(pValueLeft),as.double(pValueRight),as.integer(nPoints), symbol)
#         
#         result$pdfNormal=.jcall(z,returnSig="[[D",method="getDoubleMatrix", "pdf", simplify=TRUE)
#         result$valueNormal=.jcall(z,returnSig="[[D",method="getDoubleMatrix", "x", simplify=TRUE)
#     }
#     
#     return(result)
# }
# 
# position_returnJumpSize<-function(portfolio,symbol){
#     portfolioTemp=portfolio_create(portfolio)
#     portfolio_settings(portfolioTemp,jumpsModel='none')
#     time=position_price(portfolioTemp,symbol)[,1]
#     priceNoJumpsFilter=position_price(portfolioTemp,symbol)[,2]
#     portfolio_settings(portfolioTemp,jumpsModel='all')
#     priceJumpsFilter=position_price(portfolioTemp,symbol)[,2]
#     jumps=log(priceNoJumpsFilter)-log(priceJumpsFilter)
#     cbind(time,jumps)
# }
   
 
