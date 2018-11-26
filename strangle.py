from pandas_datareader import data  # pip install pandas_datareader
import matplotlib
#matplotlib.use('TkAgg')
import matplotlib.pyplot as plt    
import pandas as pd                


call = pd.read_csv('txoc.csv',index_col='index')
put = pd.read_csv('txop.csv',index_col='index')





cost1=call.at[9700,"close"] #long call
cost2=put.at[9500,"close"]  #long put



sp1=9700 
sp2=9500





payoff1=call.pop("payoff1")   
payoff2=call.pop("payoff2")    
Tpayoff=call.pop("Tpayoff")    #total payoff 


profit1=call.pop("profit1")   #PROFIT of short position
profit2=call.pop("profit2")    #PROFIT of long position
Tprofit=call.pop("Tprofit")    #total PROFIT 


for index in call["strike"]:
    #long call position
    if index>sp1:
        payoff1[index]=index-sp1
        
        
    else:
        payoff1[index]=0
        
    profit1[index]=payoff1[index]-cost1 #long profit 向下平移
    


    #long put position
    if index>sp2:
        payoff2[index]=0
        
    else :
        payoff2[index]=sp2-index
        
    profit2[index]=payoff2[index]-cost2 #long profit 向下平移

    
    
    
    Tpayoff[index]=payoff1[index]+payoff2[index]
    Tprofit[index]=profit1[index]+profit2[index]






print (payoff1)
print (payoff2)
print (Tpayoff)
call.insert(3,"payoff1",payoff1)
call.insert(4,"payoff2",payoff2)
call.insert(5,"Tpayoff",Tpayoff)

call.insert(6,"profit1",profit1)
call.insert(7,"profit2",profit2)
call.insert(8,"Tprofit",Tprofit)

print (call)






plt.ylim((-1000,700))
plt.plot(call["profit1"],color='red', label='Long Call profit')
plt.plot(call["profit2"],color='blue', label='Long Put profit')
plt.plot(call["Tprofit"],color='orange', label='Strangle Value')
plt.legend(loc='best')
plt.show()
    
