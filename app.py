from flask import Flask, render_template, jsonify
#from model import Model
import beer_rec
import pandas as pd

#For now, app is loading static csv file. We should move the file to resources or 
#if performance is an issue connect this app to a db. Model shouldn't be needed unless
#we have a db connection

app = Flask(__name__)
#model = Model()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/map')
def map():
    return render_template('map.html')

@app.route('/graphs')
def graphs():
    return render_template('graphs.html')

@app.route('/recs')
def red():
    return render_template('recs.html')

@app.route('/names')
#We would use this API endpoint to populate dropdown
def names():
    data = pd.read_csv('beer_reviews.csv')
    names = list(data['beer_name'].unique())
    return jsonify(names)

@app.route('/advice/<beer>')
def get_similar(beer):
    reviews = pd.read_csv('beer_reviews.csv')
    breweries = pd.read_csv('breweries.csv')
    data = pd.merge(reviews, breweries, how='inner', left_on = 'brewery_name', right_on = 'name')
    data = data.fillna(value = 0)
    new_beer = beer_rec.recommend_beer(beer)
    beer_data_row = data.loc[data['beer_name'] == new_beer]
    beer_data_row = beer_data_row.to_json(orient='index')
    return (new_beer)


if __name__ == "__main__":
    app.run(debug=True)
