import Holding
from bittrex import Bittrex

class Portfolio:

    def __init__(self):
        self.balances ={"USD":0, "ETH": 0}
        self.trades = []

    def deposit(self,s):

        self.balances['USD'] = self.balances['USD'] + s

    def withdrawal(self,w):
        self.balances['USD'] = self.balances['USD'] - s

    def addHolding(self, coin, qty, price):
        print self.balances[coin] + qty
        if self.balances[coin] + qty >= 0:
            print "good"
            h = Holding.Holding(coin,qty,price)
            if self.balances['USD'] - h.getCost() >= 0:
                self.balances[coin] = self.balances[coin] + qty
                self.balances['USD'] = self.balances['USD'] - h.getCost()
                print "Bought " + str(qty) + " " + coin + " at " + str(price)
                self.trades.append(h)

    def getReturns(self,df):
        profit = 0
        for h in self.trades:
            profit = profit + h.getReturns(df)
        return profit

    def getUSDValue(self,df):
        value = self.balances['USD'] + self.balances['ETH'] * df['weightedAverage']
        return value

    def printPortfolio(self):
        for key, value in self.balances.iteritems():
            print key + ": " + str(value)
