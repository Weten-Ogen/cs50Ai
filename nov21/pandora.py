import pandas as pd
import numpy as np

s = pd.Series([1,2,3,np.nan,5,6], index=['a','b','c','d','f','g'])
print(s)

# DataFrames

data = {
    'first_name' :['Florence', 'Marcus', 'Magaret', 'Alice','Ida'], 
    'Emp_ID': ['1','2','3','4','5'],
    'last_name': ['Obinim', 'Oware', 'Opoku','Boateng', 'Adiyiah'],
}


df_1 = pd.DataFrame(data,columns=['Emp_ID','first_name','last_name'])

data1 = {
    'first_name' :['Flora', 'Micheal', 'Morris', 'Addison','Ivy'], 
    'Emp_ID': ['6','7','8','9','10'],
    'last_name': ['Obi', 'Young', 'Kefason','Boat', 'Addae'],
}

df_2 = pd.DataFrame(data1, columns=['Emp_ID','first_name','last_name'])

# pom = pd.concat([df_1, df_2], axis=0)
print(pd.merge(df_1, df_2, on='Emp_ID', how='outer'))