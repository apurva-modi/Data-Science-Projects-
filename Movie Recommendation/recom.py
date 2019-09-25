import numpy as np
from lightfm.datasets import fetch_movielens
from lightfm import LightFM # Will we helpfull in creating a Model.

# fetch data and format it. 
data = fetch_movielens(min_rating=4.0) # only collecting the movies with the rating of 4.0 or higher
# this method will create a interaction matrix from CSV file and store it in our "data" variable as a dictionary. 
print(repr(data['train'])) # 90%
print(repr(data['test'])) # 10%

# Store our model in a variable named "model"
# Initialize a Lightfm class using a single parameter called "lose"
# Lose means a Loss function and it measures the difference between the model prediction and desired output
# We want to minimize it during training so that our model gets more accurate over time in its prediction. 
# Here we are using a Loss called WARP = Weighted Approximate-Rate PairWise.

model = LightFM(loss='wrap')
# Wrap help us create recommendation for each users by looking at the existing user rating pairs,
# and predicting ratings for each.
# It uses the gradiebt descent algorithm to iteratively find the weights 
# that imporve our prediction overtime. Using users past rating history and similar users rating.
# Content + Collaborative = Hybrid System

# Use fit method to trian our model
# fit takes 3 parameters 
model.fit(data['train'],)