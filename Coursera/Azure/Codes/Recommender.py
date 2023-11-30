#recommendation system works:
	#goes all over our options and learn what we like and then recommend us 
#fomo - > Fear of missing out :) 
"""
There are two types of recommender system.
1- Collobrative 
	* look at the history and recommend what everyhone else like 
2- Content based 
	* look at the history and recommend what you liked in the past 

"""
import numpy as np 
from lightfm.datasets import fetch_movielens 
from lightfm import LightFM 

#fetch data and format it 

data = fetch_movielens(min_rating = 4.0) 
#we are only collecting data 4.0+ rating 
#storing in a variable data(dictionary)

#printtraining and testing data 
print(repr(data['train']))
print(repr(data['test']))

#create model, our model does content + colleberative  
model = LightFM(loss = 'warp')

#train the model 
model.fit(data['train'],epochs = 30, num_threads = 2)

def sample_recommendation(mddel,data,user_ids):
	#number of users and number of movies in training data 
	n_users,n_items  = data['train'].shape

	#generate  recommendation for each user we input 
	for user_id in user_ids:

		#movies they already liked 
		known_positives =data['item_labels'][data['train'].tocsr() [user_id].indices]

		#movie our model predicts they will like 
		scores = model.predict(user_id, np.arange(n_items))

		#rank them in order of most liked to least 
		top_items = data['item_labels'][np.argsort(-scores)]

		#print out the results 
		print("User %s" %user_id)
		print("    Known Positives:")

		for x in known_positives[:3]:
			print("			%s " % x)

		print(" 	Recommended:")


		for x in top_items[:3]:
			print("			%s" % x)

sample_recommendation(model,data,[3,25,450])























