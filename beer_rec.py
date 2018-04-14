import pandas as pd
import numpy as np
from scipy.spatial import distance
reviews = pd.read_csv('beer_reviews.csv')
breweries = pd.read_csv('breweries.csv')

data = pd.merge(reviews, breweries, how='inner', left_on = 'brewery_name', right_on = 'name')
data = data.fillna(value = 0)

def similar_reviewers(beer_1, beer_2):
    reviews_1 = data.loc[data['beer_name'] == beer_1]
    reviews_2 = data.loc[data['beer_name'] == beer_2]
    same_reviewers = list(set(reviews_1['review_profilename']).intersection(reviews_2['review_profilename']))
    return same_reviewers

def get_beer_reviews(beer, reviewers):
    mask = (data.review_profilename.isin(reviewers)) & (data.beer_name==beer)
    reviews = data[mask]
    reviews = reviews[reviews.review_profilename.duplicated()==False]
    return reviews

features = ['review_overall', 'review_aroma', 'review_palate', 'review_taste', 'beer_abv']
def calculate_similarity(beer1, beer2):
    beer_1_reviewers = data[data.beer_name==beer1].review_profilename.unique()
    beer_2_reviewers = data[data.beer_name==beer2].review_profilename.unique()
    common_reviewers = set(beer_1_reviewers).intersection(beer_2_reviewers)
    
    beer_1_reviews = get_beer_reviews(beer1, common_reviewers)
    beer_2_reviews = get_beer_reviews(beer2, common_reviewers)
    
    beer_1_vals = []
    beer_2_vals = []
    for f in features:
        beer_1_vals.append(beer_1_reviews[f])
        beer_2_vals.append(beer_2_reviews[f])
    dist = distance.euclidean(beer_1_vals[0], beer_2_vals[0])
    return dist

def recommend_beer(user_beer):
    beers = np.random.choice(data['beer_name'], 60, replace = False)
    max_distance = 100
    sim_beer = "Sorry, we couldn't find anything similar! Try again?"
    for beer in beers:
        if user_beer != beer:
            print("cool")
            if len(similar_reviewers(user_beer, beer)) != 0:
                print('skipping' + beer)
                row = [beer, calculate_similarity(user_beer, beer)]
                if row[1] < max_distance:
                    print(row[1])
                    sim_beer = row[0]
            else:
                print("no common reviewers")
    return(sim_beer)