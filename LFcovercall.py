from pandas_datareader import data  # pip install pandas_datareader
import matplotlib
#matplotlib.use('TkAgg')
import matplotlib.pyplot as plt    # pip install matplotlib
import pandas as pd                # pip install pandas


call = pd.read_csv('txoc.csv',index_col='index')





sp=9600 
fprice=9800                    #contract due at 201812 at 2018/11/19
cost1=call.at[9600,"close"] 





payoff1=call.pop("payoff1")   #payoff of short position
payoff2=call.pop("payoff2")   #payoff of future part
Tpayoff=call.pop("Tpayoff")    #total payoff 


profit1=call.pop("profit1")   #PROFIT of short position
profit2=call.pop("profit2")    #PROFIT of long position
Tprofit=call.pop("Tprofit")    #total PROFIT 





for index in call["strike"]:
    #short call options position
    if index>sp:
        payoff1[index]=sp-index
        
        
    else:
        payoff1[index]=0
        
    profit1[index]=payoff1[index]+cost1 #short profit 先收權利金
    


    #long futures at 9800 position
    
    payoff2[index]=index-fprice
        
    profit2[index]=payoff2[index] #future position doesnt have cost

    
    
    
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






plt.ylim((-700,700))
plt.plot(call["profit1"],color='red', label='Short Call profit')
plt.plot(call["profit2"],color='blue', label='Long Futures profit')
plt.plot(call["Tprofit"],color='orange', label='Covered Call Value')
plt.legend(loc='best')
plt.show()
    
