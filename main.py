## Cat Simulation
## correlate peace agreements with other issues
### correlates of war????
### game theory analysis for conflict recitivism (continuation wars)

import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn import preprocessing
import matplotlib.pyplot as plt


basetable = pd.read_csv('data.csv')
print(basetable.head())

basetable_size=len(basetable)
print(basetable_size)

target_count=sum(basetable['Kyrgistan Conflict'])
print(target_count)
print(target_count/basetable_size)
X=basetable[['year','Tajikistan Conflict', 'Taj']]
