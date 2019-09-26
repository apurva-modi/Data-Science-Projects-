import numpy as np
from lightfm.datasets import fetch_movielens
from lightfm import LightFM # Will we helpfull in creating a Model.

# fetch data and format it. 
data = fetch_movielens(min_rating=4.0) # only collecting the movies with the rating of 4.0 or higher
# this method will create a interaction matrix from CSV file and store it in our "data" variable as a dictionary. 

print(repr(data['train'])) # 90%
print(repr(data['test'])) # 10%

'''
# Store our model in a variable named "model"
# Initialize a Lightfm class using a single parameter called "lose"
# Lose means a Loss function and it measures the difference between the model prediction and desired output
# We want to minimize it during training so that our model gets more accurate over time in its prediction. 
# Here we are using a Loss called WARP = Weighted Approximate-Rate PairWise.
'''

model = LightFM(loss='warp')

'''
# Wrap help us create recommendation for each users by looking at the existing user rating pairs,
# and predicting ratings for each.
# It uses the gradiebt descent algorithm to iteratively find the weights 
# that imporve our prediction overtime. Using users past rating history and similar users rating.
# Content + Collaborative = Hybrid System
'''

# Use fit method to trian our model
# fit takes 3 parameters 
# (the  dataset we want to train, the number of epochs we want to run the training for, and the number of threads we want to run this on

model.fit(data['train'],epochs=30,num_threads=2)

# epochs are number of runs we want 
# Threads is parallel computation


# Generating recommendation for our model 
def recommendation(model, data, user_ids):

    # get the numbers of users and movies in the training data
    # These are users we want to generate recommendations for
    n_users, n_movies = data['train'].shape

    '''
    # Use "for" loop to iterate through every user ID  that we input
    # resulting in a list of known positives for each
    # Considering ratings of 5 as positive and 4 or below as negative
    # to make the problem binary much simpler.
    # We will get the list of positive rating from our data in compressed sparse row format.
    '''

    # generate recommendation for each user. 
    for user_id in user_ids:
        # movies they already like
        # Below is a sub array inside our data matrix which will retrieve using the indices attribute 
        known_positves = data['item_labels'][data['train'].tocsr()[user_id].indices]

        '''
        Will we generate recommendation and store them in the scores variable 
        using the predict method of model.
        user ID as our first parameter 
        and a list of every movie - the arange method of numpy will give every number from 0 to the no. of items 
        so that we can predic the score for every movie.
        Then we will sort them in order of their scores.
        '''

        # Movies which our model predict they will be like 
        scores = model.predict(user_id, np.arange(n_movies))
        # ranked them in order of most liked to least
        top_movies = data['item_labels'][np.argsort(-scores)]

        # printing result 
        # " %s " will convert ID to a string 

        print("Users %s"%user_id)
        print("      Known positives:")
        # top 3 known movies
        for x in known_positves[:3]:  # for loop ending in the third index 
            print("           %s"%x)
        
        print("      Recommended:")
        # top 3 Recommended movies - model prediction
        for x in top_movies[:3]:
            print("               %s"%x)


recommendation(model,data,[3,25,450])