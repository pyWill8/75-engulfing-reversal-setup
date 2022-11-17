import DataFrame
import pandas as pd
import numpy as np

#once weve finished coding ill need to cut out like the first 20 range bars to account for the fact that the first few range bars could be within a big range bar, so still storing it but not including the stats should account for it.

class RangeBars:

    def __init__(self):
        self.bar_storage = {"High": 0, "Low": 0}
        DataFrame = DataFrame.df_reversed
        self.highlow = DataFrame.high_and_low
        self.close = DataFrame.candle_close
        self.h_low_c = DataFrame.high_low_close
        #self.range_bar = pd.DataFrame(bar_storage, index=[1])
        self.bullish_range_bar = {"High": 0, "Low": 0}
        self.bearish_range_bar = {"High": 0, "Low": 0}
        self.entry_price = 0
        self.pos = False
        
        

    def r_bar(self):
        #want to store the range bar value, clear and replace it when we find a close outside of the low and high.

        #In this inside bar variable we are counting the number of bars inside the range bar. 
        #The reason why we have it stored as -1 is because if not it will read as having one too many bars inside, as the initial range bar will count as 1, now its zero.
        inside_bars_count = -1
        #Pretty sure this is working as intended. We are checking if the close is outside the bar, storing in a dictionary, then continuing into the next iteration, checking against that dict values. 
        for i, row in self.h_low_c.iterrows():
            #check if the inside bar count is greater than or equal to 2, if it is then look for the next range bar and look to see if the candle after engulfs more than or equal to 75% of that close outside.
            self.entry_signal_bullish = self.bullish_range_bar["High"] - (self.bullish_range_bar["High"] -  self.bullish_range_bar["Low"]) * 0.75
            self.entry_signal_bearish = self.bearish_range_bar["Low"] +  (self.bearish_range_bar["High"] - self.bearish_range_bar["Low"]) * 0.75
            
            if inside_bars_count >= 2:
                #checking to see if we close outside the range bar. Doing a greater close and less than close seperate, so that we can find the 75% close easier.
                if row["Last"] > self.bar_storage["High"]: #bullish close outside the range bar. 
                    #storing the close above the 2+ inside bars. 
                    self.bullish_range_bar["High"] = row["High"]
                    self.bullish_range_bar["Low"] = row["Low"] 
                    try:
                        if self.h_low_c.iloc[i+1]["Last"] < self.entry_signal_bullish:
                            self.entry_price = self.h_low_c.iloc[i+1]["Last"]
                            self.pos = True # position set to True, meaning we are in a trade, can then do an if statement checking if we are in a trade, so we cant be in 2 trades at once. If we then exit, its then set to 0.
                    except:
                        continue
                    #if df.iloc[i+1] is equal to or greater than engulfing 75% of that range bar outside, then enter. 
                    #to get the 75% of the range bar close outside we do high-low / 4 * 3, and then round(num*4)/4
                    # we need to check if the range bar is bullish or bearish , we can probs do this by seeing if the close is greater than the high or less than the low. 
                if row["Last"] < self.bar_storage["Low"]:  #bearish close outside the range bar.
                    self.bearish_range_bar["High"] = row["High"]
                    self.bearish_range_bar["Low"] = row["Low"]
                    try:
                        if self.h_low_c.iloc[i+1]["Last"] > self.entry_signal_bearish:
                            self.entry_price = self.h_low_c.iloc[i+1]["Last"]
                            self.pos = True # position set to True, meaning we are in a trade, can then do an if statement checking if we are in a trade, so we cant be in 2 trades at once. If we then exit, its then set to 0.
                    except:
                        pass
            if self.pos == False:
                if row["Last"] > self.bar_storage["High"] or row["Last"] < self.bar_storage["Low"]:
                    self.bar_storage["High"] = row["High"]
                    self.bar_storage["Low"] = row["Low"]
                    inside_bars_count = -1
                inside_bars_count += 1
            #print(self.h_low_c.iloc[i+1]["Last"])
            #print(self.entry_price)
            #if we have entered
            if self.pos == True:
                #use a for loop from the current entry to see where we exit.                 
            else:
                continue
                
            
            
    def tracking_trades(self):   
        # if we take out the engulfing candles high/low we exit on a loss, and for now take profits can be the initial range bar low/high, 
        # adjusting the total by getting the difference in entry price and exit price and multiplying by 4(so we are making £1 per tick)
        print("hi")




            
            
            




    #maybe use 25th percentile of the range bar to calculate if we get tht 75% close.
    
                
        



range_bars = RangeBars()
range_bars.r_bar()
range_bars.tracking_trades()

#if __name__ == "__main__":

    




