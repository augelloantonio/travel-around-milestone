import os
import json
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 

#Inizialize Flask
app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'travel_around'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')

mongo = PyMongo(app)


#Set as homepage my index.html
@app.route('/')
def index():
    return render_template("index.html", cities=mongo.db.cities.find(),
    city_category=mongo.db.city_category.find())
    

@app.route('/add_city')
def add_city():
    country=[]
    with open('data/countries.json') as json_file:
        json_file = json.loads(json_file.read())
        return render_template('addcity.html', country=json_file,
        city=mongo.db.cieties.find())
    
    
@app.route('/insert_city', methods=['POST'])
def insert_city():
    cities = mongo.db.cities
    cities.insert_one(request.form.to_dict())
    return redirect(url_for('index'))


#Permitt the server to run the web app
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get("PORT")),
            debug=True)
            