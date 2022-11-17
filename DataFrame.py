import pandas as pd
import numpy as np
import csv


df = pd.read_csv("4hr ES.csv")
#reversing the data, so we start back and work towards the present
df_reversed = df.iloc[::-1].reset_index(drop=True)


#getting various rows and removing the BarChart print at the bottom (now top)
high_and_low = df_reversed[["High", "Low"]][1:]
candle_close = df_reversed["Last"][1:]
high_low_close = df_reversed[["High", "Low", "Last"]][1:]
high_low_close_time_open = df_reversed[["Time", "Open", "High", "Low", "Last"]][1:]
high_low_close_time_open.rename(columns={"Last": "Close"}, inplace=True)

#print(high_low_close_time_open)


#turning the time column into a datetime object










