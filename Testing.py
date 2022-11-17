import DataFrame
import pandas as pd
import mplfinance as mpf
import numpy as np
from backtesting import Backtest, Strategy

#creating a random entry stock trader

df = pd.read_csv("4hr ES.csv")

df["signal"] = np.random.randint(-1, 3, len(df)) #-1 is short, 1 is long, 0 is do nothing, 2 is close position

#turning the time column into a datetime object
df["Time"] = pd.to_datetime(df["Time"])
df = df.set_index("Time")
#reversing the data, so that we are starting in the past and working towards the present
df = df.iloc[::-1]
#removing the first row
df = df[1:]

#removing the Symbol column, change and %chg columns, and open interest
df = df.drop(["Symbol", "Change", "%Chg", "Open Int"], axis=1)
df.rename(columns={"Last": "Close"}, inplace=True)


class Signal(Strategy):
    def init(self):
        pass

    def next(self):
        if self.data.signal == 1:
            if not self.position:
                self.buy()
        elif self.data.signal == -1:
            if not self.position:
                self.sell()
        elif self.data.signal == 2:
            if self.position:
                self.position.close()
            

bt = Backtest(df, Signal, cash=10000)
stats = bt.run()
#bt.plot()
print(stats)

#wanting to run a random binary distribution playing out this strategy 10000 times on this data set





    






