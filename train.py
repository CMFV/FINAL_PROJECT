import pandas as pd
import numpy as np
import sklearn
from sklearn import preprocessing

df_me_data=pd.read_csv('me_diet_data.csv')
df_me_data.drop(columns=['Unnamed: 0', 'Name'], inplace=True)

labels= df_me_data['Group']
