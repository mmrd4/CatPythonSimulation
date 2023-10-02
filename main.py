## Cat Simulation
## correlate peace agreements with other issues
### correlates of war????
### game theory analysis for conflict recitivism (continuation wars)

import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn import preprocessing
import matplotlib.pyplot as plt

# Step 1: Acquire a Peace Agreement Dataset
#download Zip
#extract CSV from Zip
#import CSV

####### data needed
#Armed conflict dataset
#non-state conflict-obe
#peace agreements-obe
#violence political protest-obe
#ethnic one-sided violence-obe
#conflict termination-obe
#nonstate conflict issues-obe
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


# Step 4: Parameterize the Model
# Assign values to variables

# Step 5: Run Simulations
X = data.drop(columns=['year'])#'conflict_id','location','side_a','side_b','side_b_2nd','territory_name','start_date','start_prec','start_date2','start_prec2','ep_end_date','ep_end_prec','gwno_a','gwno_a_2nd','gwno_b','gwno_b_2nd','gwno_loc','version','year'])
X['side_a_id'] = X['side_a_id'].astype(float)
X['side_b_id'] = X['side_b_id'].astype(float)
X['incompatibility'] = X['incompatibility'].astype(float)
X['intensity_level'] = X['intensity_level'].astype(float)
X['cumulative_intensity'] = X['cumulative_intensity'].astype(float)
X['type_of_conflict'] = X['type_of_conflict'].astype(float)
X = X.values
y = data['year']

model = LogisticRegression(solver ='newton-cholesky').fit(X, y)
model.score(X, y)
model.coef_
# side_a_id,side_b_id,incompatibility,intensity_level,cumulative_intensity,type_of_conflict,ep_end
#incompatibility: 1= Incompatibility about territory  2= Incompatibility about government 3= Incompatibility about government AND territory
# intensity level: 1 minor, 2 War
# cumulative_intensity: 0 under 1000, 1 over 1000
# type 1 = extrasystemic (between a state and a non-state group outside its own territory, where the government side is fighting to retain control of a territory outside the state system) 2 = interstate (both sides are states in the Gleditsch and Ward membership system). 3 = intrastate (side A is always a government; side B is always one or more rebel groups; there is no involvement of foreign governments with troops, i.e. there is no side_a_2nd or side_b_2nd coded) 4 = internationalized intrastate (side A is always a government; side B is always one or more rebel groups; there is involvement of foreign governments with troops, i.e. there is at least ONE side_a_2nd or side_b_2nd coded)
prediction=model.predict(np.array([[703,702,3,2,1,2,0]]))
print(prediction)
# Step 6: Analyze Results
# Example: Visualize coefficients
#plt.bar(X.columns, model.coef_[0])
#plt.show()
