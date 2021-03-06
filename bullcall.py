from pandas_datareader import data  # pip install pandas_datareader
import matplotlib
#matplotlib.use('TkAgg')
import matplotlib.pyplot as plt    # pip install matplotlib
import pandas as pd                # pip install pandas


call = pd.read_csv('txoc.csv',index_col='index')





cost1=call.at[9600,"close"] #short
cost2=(call.at[9500,"close"]) #long




sp1=9600 #short
sp2=9500 #long




payoff1=call.pop("payoff1")   #payoff of short position
payoff2=call.pop("payoff2")    #payoff of long position
Tpayoff=call.pop("Tpayoff")    #total payoff 


profit1=call.pop("profit1")   #PROFIT of short position
profit2=call.pop("profit2")    #PROFIT of long position
Tprofit=call.pop("Tprofit")    #total PROFIT 


for index in call["strike"]:
    if index>sp1:
        payoff1[index]=sp1-index
        
        
    else:
        payoff1[index]=0
        profit1[index]=cost1
    
    if index>sp2:
        payoff2[index]=index-sp2
        
    else :
        payoff2[index]=0
        
    
    
    profit1[index]=payoff1[index]+cost1
    Tpayoff[index]=payoff1[index]+payoff2[index]
    profit2[index]=payoff2[index]-cost2

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
plt.plot(call["profit2"],color='blue', label='Long Call profit')
plt.plot(call["Tprofit"],color='orange', label='Bullspread(call) Value')
plt.legend(loc='best')
plt.show()
    

