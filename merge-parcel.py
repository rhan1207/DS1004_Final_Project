
# coding: utf-8

# In[30]:

import pandas as pd
import numpy as np
from pandas import DataFrame

data1 = pd.read_csv('2012 NYC Brooklyn NYC.txt',sep="\t")
data2 = pd.read_csv('2012 NYC Brooklyn Assessment.txt',sep="\t")
merged = pd.merge(data1,data2, on=['parcel_id'])
merged.to_csv(r'/Users/apple/Downloads/2012_NYC_co/pandas.txt', sep=' ', mode='a')

