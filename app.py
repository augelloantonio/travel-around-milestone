"""
~ Travel Around ~ is a web site build for travellers that would like to know some basic informations on the cities aroud the world.
The website is build as Full Stack Developement using data from MongoDB.
The CRUD (Create - Read - Update -Delete) rule has been applied. The user can read the informations, can Login and add, update or delete 
the informations presents on the website.
"""

import os
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


#Redirect the user who whant to add a new city to a new page with the input form
@app.route('/add_city')
def add_city():
    return render_template('addcity.html',
    city=mongo.db.cieties.find())
    
    
# Send the info provided in the form to MongoDB
@app.route('/insert_city', methods=['POST'])
def insert_city():
    cities = mongo.db.cities
    cities.insert_one(request.form.to_dict())
    return redirect(url_for('index'))

#Edit the data
@app.route('/edit_city/<city_id>')
def edit_city(city_id):
    the_city = mongo.db.cities.find_one({"_id": ObjectId(city_id)})
    all_cities =  mongo.db.cities.find()
    return render_template('editcity.html', city=the_city,
                           cities=all_cities)
                           
# Updata the datas and send them to MongoBD
app.route('/update_city/<city_id>', methods=['POST'])
def update_city(city_id):
    cities = mongo.db.cities
    cities.update( {'_id': ObjectId(city_id)},
    {
        'city_name':request.form.get('city_name'),
        'city_country':request.form.get('city_coutry'),
        'city_population': request.form.get('city_population'),
        'city_description': request.form.get('city_description'),
        'city_must_see':request.form.get.getlist('city_must_see'),
        'city_category':request.form.getlist('city_category'),
        'city_author':request.form.get('city_author'),
        'city_image':request.form.get('city_image')
    })
    return redirect(url_for('index'))


#Permitt the server to run the web app
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get("PORT")),
            debug=True)
            