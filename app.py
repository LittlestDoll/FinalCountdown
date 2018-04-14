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
    names = ['90 Minute IPA',
            'India Pale Ale',
            'Old Rasputin Russian Imperial Stout',
            'Sierra Nevada Celebration Ale',
            'Two Hearted Ale',
            'Arrogant Bastard Ale',
            'Stone Ruination IPA',
            'Sierra Nevada Pale Ale',
            'Stone IPA (India Pale Ale)',
            'Pliny The Elder']
    return jsonify(names)

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
