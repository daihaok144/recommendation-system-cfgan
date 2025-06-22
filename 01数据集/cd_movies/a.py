import numpy as np
import pandas as pd
data  = pd.read_csv('test.csv',sep='\t',names=['uid','iid','rate','time'])

data = data.drop_duplicates(['uid','iid','rate','time'], keep='first')
data.to_csv('test1.csv',index=False,sep='\t')