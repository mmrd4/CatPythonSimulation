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

####### data needed
#Armed conflict dataset
#non-state conflict
#peace agreements
#violence political protest
#ethnic one-sided violence
#conflict termination
#nonstate conflict issues
# EXTERNAL SUPPORT
#UCDP Managing Intrastate Low-intensity Conflict (MILC) Dataset
#UCDP Managing Intrastate Conflict (MIC) Dataset

### what is the probablility of a country going to war with the above data




#####



# Assuming you have a CSV file named 'peace_agreements.csv'
data = pd.read_csv('UcdpPrioConflict_v23_1.csv')


# Step 2: Define Variables
# Identify and preprocess relevant variables

# Step 3: Model Selection
# Choose a modeling technique (e.g., logistic regression)
model = LogisticRegression()

# Step 4: Parameterize the Model
# Assign values to variables

# Step 5: Run Simulations
x = data#.drop(columns=['conflict_id','location','side_a','side_b','side_b_2nd','territory_name','start_date','start_prec','start_date2','start_prec2','ep_end_date','ep_end_prec','gwno_a','gwno_a_2nd','gwno_b','gwno_b_2nd','gwno_loc','version','year'])
x['side_a_id'] = x['side_a_id'].astype(float)
x['side_b_id'] = x['side_b_id'].astype(float)
x['incompatibility'] = x['incompatibility'].astype(float)
x['intensity_level'] = x['intensity_level'].astype(float)
x['cumulative_intensity'] = x['cumulative_intensity'].astype(float)
x['type_of_conflict'] = x['type_of_conflict'].astype(float)

y = data['year']

model.fit(x, y)

model.predict('703')

# Step 6: Analyze Results
# Example: Visualize coefficients
plt.bar(x.columns, model.coef_[0])
plt.show()
