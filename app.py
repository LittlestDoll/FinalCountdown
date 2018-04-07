from flask import Flask, render_template, jsonify
from model import Model

app = Flask(__name__)
model = Model()

@app.route('/')
def home():
    """Return the dashboard homepage."""
    return render_template('index.html')

@app.route('/app.js')
def appjs():
    return app.send_static_file('app.js')

@app.route('/names')
def names():
    """List of beer names.
    Returns a list of beer names
    """
    names = model.get_names()
    return jsonify(names)

@app.route('/data')
def otu():
    """Table of data
    """
    return jsonify(data)

@app.route('/metadata/<beer>')
def metadata(sample):
    """MetaData for a given beer - as a dict

    Returns a json dictionary of beer metadata
    """
    return jsonify(model.get_beer(beer_name))         

if __name__ == "__main__":
    app.run(debug=True)