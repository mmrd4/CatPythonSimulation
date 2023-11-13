## Cat Simulation
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter


df = pd.read_csv('Data.csv')
ndf = pd.read_csv('Data_withpredictions to 2032.csv')
year = ndf['year']
ndf=ndf.drop('year',axis=1)
df=df.drop('year',axis=1)

predictors = ['Tajikistan Conflict','Kyrgistan Conflict','Tajikistan Average Precipitation','Tajikistan GDP','Kyrgistan Average Precipitation','Kyrgistan GDP','Tajikistan Military Expenditures','Kyrgistan Military Expenditures','Tajikistan Freshwater withdrawals','Kyrgistan Freshwater withdrawals']
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
plt.subplots(figsize=(10, 8))
plt.plot(year, yhat)
# only one line may be specified; full height
plt.axvline(x = 2023, color = 'r', label = 'axvline - full height')
plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
plt.title("Probability of Conflict Recidivism between Kyrgistan and Tajikistan")
plt.xlabel("Year")
plt.ylabel("Probablility of Conflict Recidivism")
plt.xticks(np.arange(1998, 2033, 1), rotation ='vertical')

# Show the plot
plt.show()

weights = model.coef_
print ("weights")
print(weights)
