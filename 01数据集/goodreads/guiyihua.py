import pandas as pd

data = pd.read_csv('all_train_pop.csv',names=['user','item','pop_value','time'],header=0)

data.to_csv('all_train_pop1.csv',index=False)