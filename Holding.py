import pandas as pd
import datetime

class Holding:

    def __init__(self, coin, qty, price):

        self.coin = coin
        self.qty = qty
        self.price = price
        self.datetime = datetime.datetime.now().time()

    def getCost(self):
        return self.qty*self.price

    def getReturns(self, df):
        return getValue(df) - getCost()

    def getValue(self,df):
        return df['weightedAverage'] * self.qty
