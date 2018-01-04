# -*- coding: utf-8 -*-

import Portfolio
import Algorithm
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date
from time import mktime

#intial capital, also buys benchmark
cash = 100

#currencyPair
pair = "USDT_ETH"

#Start Date (y,m,d)
start = date(2017,1,20)

#End Date (y,m,d)
end = date(2017,12,25)

#Benchmark, uses all inital capital on currency
benchmark = "ETH"

#candlestick time interval- valid values are: 300, 900, 1800, 7200, 14400, and 86400 (seconds)
interval = 14400

#data we'll be backtasting over
df = pd.read_json("https://poloniex.com/public?command=returnChartData&currencyPair="+pair+"&start="+str(mktime(start.timetuple()))+"&end="+str(mktime(end.timetuple()))+"&period="+ str(interval), orient = 'columns')
print df
#computes value based on a df row
def getBenchmarkValue(d):
    return benchmarkQty * d['weightedAverage']

#computes returns as a percent over the span of a df
def getBenchmarkReturns(d):
    return  (d.tail(1).iloc[0]['weightedAverage'] - d.head(1).iloc[0]['weightedAverage'])/d.head(1).iloc[0]['weightedAverage']

#initializations
algo = Algorithm.Algorithm()
pf = Portfolio.Portfolio()
pf.deposit(cash)
compareDf = pd.DataFrame()
benchmarkQty = cash / df.head(1).iloc[0]['weightedAverage']

#runs logic on the current row, updates value of portfolio and benchmark for results
for index, row in df.iterrows():
    print index
    algo.algorithmLogic(row,pf)
    entry = pd.DataFrame([[pf.getUSDValue(row),getBenchmarkValue(row)]],columns = {'Portfolio', 'Benchmark'})
    compareDf = pd.concat([compareDf,entry],axis=0,ignore_index=True)

#Print results
print "\nRESULTS: \n"
print "\tInitial Portfolio: " + str(cash) + " USD"
print "\tFinal Portfolio: " + str(compareDf.tail(1)['Portfolio']) + " USD"
print "\tPct Change: " + str((compareDf.tail(1).iloc[0]['Portfolio']-cash)/cash * 100) + "\n"
print "\tFinal Benchmark Price (" + benchmark + "):"+ str(df.tail(1).iloc[0]['weightedAverage'])
print "\tFinal Benchmark Portfolio Value (" + benchmark + "):" + str(compareDf.tail(1).iloc[0]['Benchmark'])
print "\tBenchmark Pct Change: " + str((compareDf.tail(1).iloc[0]['Benchmark']-cash)/cash * 100) + "\n"
print pf.printPortfolio()

#Plot results
compareDf.plot()
plt.savefig("results.png")
