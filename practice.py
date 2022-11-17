import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

data = {'Name':['Tom', 'nick', 'krish', 'jack'],
        'Age':[20, 21, 19, 18]}

df = pd.DataFrame(data)


#print(df.iloc[0+1])
#testing trying to get the next index. 
#try:
  #  for i, row in df.iterrows():
  #      print(df.iloc[i+1])
#except:
   #pass

#print(round(5.0625*4)/4)  

#print(4200 - (4200 - 4198) * 0.75)


x = str(234235)
lst = []
for i in x:
        lst.append(i)
lst.reverse()
print(lst)