import DataFrame
import pandas as pd
import mplfinance as mpf
import numpy as np
import JustRBars

df = JustRBars.df

#turning all the NaN values in df.entry to 0
df["entry"].fillna(0, inplace=True)
#print(df.head(50))
#so what im thinking is that we iterate through df, if we have a entry point we store the entry price, stop and take_profit

#IT LOOKS LIKE THIS IS WORKING AS INTENDED, HOWEVER ILL NEED TO DO MORE TETSING TO MAKE SURE ITS WORKING CORRECTLY.    Not sure that situations where im already in a trade is working. 
class GettingExits:
    
    def __init__(self):
        self.df = df
        self.entry_info = {"entry": 0, "stop": 0, "take_profit": 0}  # storing the entry candles info
        #self.storing_the_index = 0 # storing the 
        self.in_trade_or_not = False
        self.bullish = 0  #meaning that we are in a bullish trade
        self.bearish = 0  #meaning that we are in a bearish trade


    def get_exit_points(self):
        #iterate through the dataframe
        for index, row in df.iterrows():
            if self.in_trade_or_not == True and self.bullish == 1:
                    #checking to see if we have hit the stop or take profit on this iteration
                    if row["Low"] <= self.entry_info["stop"] or row["High"] >= self.entry_info["take_profit"]:
                        self.df.at[index, "entry"] = 2 # meaning that we have closed a position at that candle
                        self.in_trade_or_not = False #so that we dont have overlapping trades
                        self.bullish = 0
                        self.entry_info = {"entry": 0, "stop": 0, "take_profit": 0}
                        continue

            if self.in_trade_or_not == True and self.bearish == -1:
                    #checking to see if we have hit the stop or take profit on this iteration
                    if row["High"] >= self.entry_info["stop"] or row["Low"] <= self.entry_info["take_profit"]:
                        self.df.at[index, "entry"] = 2 # meaning that we have closed a position at that candle
                        self.in_trade_or_not = False #so that we dont have overlapping trades
                        self.bearish = 0
                        self.entry_info = {"entry": 0, "stop": 0, "take_profit": 0}
                        continue


            if row["entry"] == 1 and self.in_trade_or_not == False: # getting bullish entry and checking to see that we are not already in a trade.
                self.entry_info["entry"] = row["Close"]
                self.entry_info["stop"] = row["stop"]
                self.entry_info["take_profit"] = row["take_profit"]
                self.in_trade_or_not = True
                self.bullish = 1
                #self.storing_the_index = index      #i dont think we need this actually. 

            elif row["entry"] == -1 and self.in_trade_or_not == False: #a bearish setup
                self.entry_info["entry"] = row["Close"]
                self.entry_info["stop"] = row["stop"]
                self.entry_info["take_profit"] = row["take_profit"]
                self.in_trade_or_not = True
                self.bearish = -1
       
        return df
                


gettingexits = GettingExits()
df = gettingexits.get_exit_points()
#renaming df entry to signal
df.rename(columns={"entry": "Signal"}, inplace=True)
#print(df.head(20))