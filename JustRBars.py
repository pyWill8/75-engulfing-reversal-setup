import DataFrame
import pandas as pd
import mplfinance as mpf
import numpy as np
pd.set_option("display.max_rows", None)
df = DataFrame.high_low_close_time_open

class EngulfingSetup:

    def __init__(self):
        self.current_range_bar = {"High": 0, "Low": 0}
        self.inside_count = 0
        self.df = df
        self.bullish_range_bar = {"High": 0, "Low": 0}
        self.bearish_range_bar = {"High": 0, "Low": 0}

    def getting_rb(self):
            #check to see if the current iteration closes outside the current range bar, if so we want to check the next candle gets that engulfing close, which equals an entry, we see if the stop price or tp is hit.
        #iterating through and finding all the range bars, and also counting the number of consecutive inside bars. Just need to figure out how to do a new method that can work with that 
  
        for i, row in self.df.iterrows():
            
            if self.inside_count >= 2:
                #HAVING AN ISSUE WITH THIS SECTION, NOT PRINTING THE CORRECT ENTYR SIGNALS. notice how its not saying bearish_entry at all
                if row["Close"] > self.current_range_bar["High"]:  #checking if closed outside of a 2+ inside bar range bar to the upside.

                    self.bullish_range_bar["High"] = row["High"]
                    self.bullish_range_bar["Low"] = row["Low"]
                    self.entry_signal_bearish = self.bullish_range_bar["High"] \
                            - (self.bullish_range_bar["High"] -  self.bullish_range_bar["Low"]) * 0.75   #entry_signal_bearish is for a bullish closures reversal.
                    try:
                        if self.df.iloc[i]["Close"] < self.entry_signal_bearish and self.df.iloc[i]["Close"] > self.current_range_bar["Low"]:  #so it seems that self.df.iloc[i+1]["Close"] is getting the candle after the correct entry price, i wonder if the i+1 is giving 2 iterations ahead instead of one. 
                            self.df.at[i+1, "entry"] = -1 #meaning a bearish entry       
                            #self.df.at[i, "bear75"] = self.entry_signal_bearish      #inputs the 75% engulfing level into the dataframe
                            #self.df.at[i, "num"] = self.df.iloc[i]["Close"]
                            self.df.at[i+1, "stop"] = row["High"] - .50 # stop is the the close outsides high + .50 for a buffer
                            self.df.at[i+1, "take_profit"] = self.current_range_bar["High"] - (self.current_range_bar["High"] - self.current_range_bar["Low"]) * 2 #take profit is the current range bar high - 2x the range bar size
                    except:
                        continue
                    
                if row["Close"] < self.current_range_bar["Low"]:  #checking if closed outside of a 2+ inside bar range bar to the upside.

                    self.bearish_range_bar["High"] = row["High"]
                    self.bearish_range_bar["Low"] = row["Low"]
                    self.entry_signal_bullish = self.bearish_range_bar["Low"]\
                            +  (self.bearish_range_bar["High"] - self.bearish_range_bar["Low"]) * 0.75
                    try:
                        if self.df.iloc[i]["Close"] > self.entry_signal_bullish and self.df.iloc[i]["Close"] < self.current_range_bar["High"]:
                            self.df.at[i+1, "entry"] = 1 # meaning a bullish entry
                            #self.df.at[i, "bull75"] = self.entry_signal_bullish
                            #self.df.at[i, "num"] = self.df.iloc[i]["Close"]
                            self.df.at[i+1, "stop"] = row["Low"] - .50 # stop is the close outsides low + .50 for a buffer.     I may change the stop at somepoint and maybe make it the low of the 2. 
                            self.df.at[i+1, "take_profit"] = self.current_range_bar["Low"] + (self.current_range_bar["High"] - self.current_range_bar["Low"]) * 2   #take profit is the low of the 2 range bars + 2 range bars of the current range bar
                    except:
                        continue
                

            if row["Close"] > self.current_range_bar["High"] or row["Close"] < self.current_range_bar["Low"]:
                self.current_range_bar["High"] = row["High"]
                self.current_range_bar["Low"] = row["Low"]
                self.df.at[i, "range_bar"] = 0  # True == 0, is a range bar
                self.inside_count = 0
                self.df.at[i, "inside_bar_count"] = self.inside_count
                #if the current inside bar coutnt >= 2, then we to see if we close outside  (would need to be the last iteration was greater than or = to 2).
            else:
                self.df.at[i, "range_bar"] = 1 # False == 1, not a range bar
                self.inside_count += 1
                self.df.at[i, "inside_bar_count"] = self.inside_count
        
        return df
        

range_bars = EngulfingSetup()
df = range_bars.getting_rb()
#print(df)

#def entry_signal():
#    print(df)
#entry_signal()





