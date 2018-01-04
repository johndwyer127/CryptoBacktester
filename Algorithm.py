

class Algorithm:

    ##algo specific vars/indicators


    def __init__(self):
        self.name = "BasicAlgorithm"
        self.average = 0;
        self.total = 0;

    def algorithmLogic(self, row, Portfolio):
        wa = row['weightedAverage']
        if self.average == 0:
            self.average = wa
            self.total = 1

        else:

            if wa<self.average*0.95:
                Portfolio.addHolding("ETH", 0.01, wa)
            elif wa>self.average*1.05:
                Portfolio.addHolding("ETH",0.01, wa)

            self.total = self.total + 1

            self.average = (self.average * (self.total-1) + wa) / self.total
