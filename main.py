## Cat Simulation
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


df = pd.read_csv('data.csv')
ndf = pd.read_csv('Data_withpredictions to 2032.csv')

predictors = ['year','Tajikistan Conflict','Kyrgistan Conflict','Tajikistan Average Precipitation','Tajikistan GDP','Kyrgistan Average Precipitation','Kyrgistan GDP','Tajikistan Military Expenditures','Kyrgistan Military Expenditures','Tajikistan Freshwater withdrawals','Kyrgistan Freshwater withdrawals']
result = ['Taj vs Kyrg']
X=df[predictors]
Xpredict=ndf[predictors]
y=df[result]
# Train a model on the training set
model = LinearRegression()
model.fit(X, y)
print("fitted")


# Use the model to predict future events
yhat = model.predict(Xpredict)
print('Future event:', yhat)

# Plot the data
plt.plot(Xpredict['year'], yhat)
# only one line may be specified; full height
plt.axvline(x = 2023, color = 'r', label = 'axvline - full height')
# Show the plot
plt.show()
