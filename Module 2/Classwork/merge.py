import pandas as pd 

Df1= pd.DataFrame( { 'A': [1,2,3,4], 'B': ['A','B','C','D']})
Df2= pd.DataFrame( { 'A': [1,2,3,4], 'D': ['a','b','c','d']})
pd.merge(Df1,Df2)
