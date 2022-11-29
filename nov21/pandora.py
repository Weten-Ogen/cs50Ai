import pandas as pd
import numpy as np

s = pd.Series([1,2,3,np.nan,5,6], index=['a','b','c','d','f','g'])
print(s)

# DataFrames

data = {
    'Gender' :['F', 'M', 'M'], 
    'Emp_ID': ['E01','E02','E03'],
    'Age': [25, 22, 24],
}

df = pd.DataFrame(data,columns=['Emp_ID','Gender','Age'])
print(df)