from flask import Flask, render_template, jsonify, request
#from model import Model
import beer_rec
import pandas as pd

#For now, app is loading static csv file. We should move the file to resources or 
#if performance is an issue connect this app to a db. Model shouldn't be needed unless
#we have a db connection

app = Flask(__name__)
data = pd.read_csv('beer_reviews.csv')
names = list(data['beer_name'].unique())
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

@app.route('/beer_search')
#We would use this API endpoint to populate dropdown
def search():
    query = request.args.get('query').lower()
    search_results = [beer for beer in names if beer.lower().find(query) != -1]
    return jsonify(search_results)


@app.route('/advice/<beer>')
def get_similar(beer):
    new_beer = beer_rec.recommend_beer(beer)
    data = beer_rec.data
    beer_reviews = data.loc[data['beer_name'] == new_beer]
    if len(beer_reviews) == 0:
        return '{"error": "no results"}'
    beer_json = beer_reviews.iloc[0].to_json(orient='index')
    return beer_json


if __name__ == "__main__":
    app.run(debug=True)
