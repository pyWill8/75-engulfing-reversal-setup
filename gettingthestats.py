import DataFrame
import pandas as pd
import mplfinance as mpf
import numpy as np
import gettingexitpoints
from backtesting import Backtest, Strategy 


df = gettingexitpoints.df

df["Time"] = pd.to_datetime(df["Time"])
df = df.set_index("Time")
#cleaning up the dataframe, removing the columns we don't need, inside_bar_count, stop and take profit
df = df.drop(["inside_bar_count", "stop", "take_profit", "range_bar"], axis=1)
#print(df.head(20))

# creating a class that buys if df.signal is 1, closes if its 2, shorts if its -1, does nothing if its 0
class SmaCross(Strategy):
    def init(self):
        pass

    def next(self):
        if self.data.Signal == 1:
            self.buy()
        elif self.data.Signal == -1:
            self.sell()
        elif self.data.Signal == 2:
            self.position.close()
        
bt = Backtest(df, SmaCross, cash=10000)
stats = bt.run()
#print(stats)
bt.plot()
#so we have a few timeframes that are producing a small profit, what im thinking of doing is fidilling with stops and entrys slightly, perhaps entering on candle close and having perhaps wider stops and tighter take profits.








    