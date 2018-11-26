from pandas_datareader import data  # pip install pandas_datareader
import matplotlib
#matplotlib.use('TkAgg')
import matplotlib.pyplot as plt    # pip install matplotlib
import pandas as pd                # pip install pandas
import time

put = pd.read_csv('txop.csv',index_col='index')





cost1=put.at[9600,"close"] #short
cost2=put.at[9500,"close"] #long




sp1=9600 #short
sp2=9500 #long




payoff1=put.pop("payoff1")   #payoff of short position
payoff2=put.pop("payoff2")    #payoff of long position
Tpayoff=put.pop("Tpayoff")    #total payoff 


profit1=put.pop("profit1")   #PROFIT of short position
profit2=put.pop("profit2")    #PROFIT of long position
Tprofit=put.pop("Tprofit")    #total PROFIT 


for index in put["strike"]:
    
    if index>sp1:
        payoff1[index]=0
        profit1[index]=cost1
        
        
    else:
        payoff1[index]=index-sp1
    
    
    if index>sp2:
        payoff2[index]=0
        
    else :
        payoff2[index]=sp2-index
        
    
    Tpayoff[index]=payoff1[index]+payoff2[index]
    
    profit1[index]=payoff1[index]+cost1
    profit2[index]=payoff2[index]-cost2

    Tprofit[index]=profit1[index]+profit2[index]






print (payoff1)
print (payoff2)
print (Tpayoff)
put.insert(3,"payoff1",payoff1)
put.insert(4,"payoff2",payoff2)
put.insert(5,"Tpayoff",Tpayoff)

put.insert(6,"profit1",profit1)
put.insert(7,"profit2",profit2)
put.insert(8,"Tprofit",Tprofit)

print (put)






plt.ylim((-700,700))
plt.plot(put["profit1"],color='red', label='Short Put profit')
plt.plot(put["profit2"],color='blue', label='Long Put profit')
plt.plot(put["Tprofit"],color='orange', label='Bullspread(put) Value')
plt.legend(loc='best')
plt.show()
    

