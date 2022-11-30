import numpy as np 
import pandas as pd

df = pd.DataFrame(
    {
        'Names':['jack','jane','jack', 'jane', 'jack', 'jane', 'jack', 'jane'],
        'states': ['SFO','SFO','NYK','CA', 'NYK','NYK', 'SFO', 'CA'],
        'grades': ['A','A','B','A','C','B','C','A'],
        'age':np.random.uniform(24, 50, size=8),
        'salary': np.random.uniform(3000, 5000, size=8),
    }
)


print(pd.pivot_table(df , values='age', index=['Names', 'states'], columns=['grades']))

