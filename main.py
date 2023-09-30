## Cat Simulation
## correlate peace agreements with other issues
### correlates of war????
### game theory analysis for conflict recitivism (continuation wars)


import pandas as pd
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt

# Step 1: Acquire a Peace Agreement Dataset
#download Zip
#extract CSV from Zip
#import CSV

# Assuming you have a CSV file named 'peace_agreements.csv'
data = pd.read_csv('UcdpPrioConflict_v23_1.1.csv')


# Step 2: Define Variables
# Identify and preprocess relevant variables

# Step 3: Model Selection
# Choose a modeling technique (e.g., logistic regression)
model = LogisticRegression()

# Step 4: Parameterize the Model
# Assign values to variables

# Step 5: Run Simulations
x = data.drop(columns=['location','ep_end_date', 'version', 'territory_name', 'side_b_2nd', 'side_b', 'side_a', 'side_a_2nd', 'start_date2', 'start_date', 'year', 'conflict_id'])
x['side_a_id']=x['side_a_id'].tolist()
x['side_b_id']=x['side_b_id'].tolist()
#x['gwno_a_2nd']=x['gwno_a_2nd'].tolist()
x['gwno_loc']=x['gwno_loc'].tolist()
x['gwno_a']=x['gwno_a'].tolist()

y = data['year']

model.fit(x, y)

# Step 6: Analyze Results
# Example: Visualize coefficients
plt.bar(x.columns, model.coef_[0])
plt.show()
