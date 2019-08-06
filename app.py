import os
import json, pymongo
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 
from time import ctime

#Inizialize Flask
app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'travel_around'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')

mongo = PyMongo(app)

#Set as homepage my index.html
@app.route('/')
def index():
    with open('data/countries.json') as json_file:
        json_file = json.loads(json_file.read())
    return render_template("index.html", cities=mongo.db.cities.find().sort('added_time', pymongo.DESCENDING), cities_carousel=mongo.db.cities.find(), country=json_file)
    
# Connect to the database file and add a new city 
@app.route('/add_city')
def add_city():
    country=[]
    with open('data/countries.json') as json_file:
        json_file = json.loads(json_file.read())
        return render_template('addcity.html', country=json_file,
        city=mongo.db.cieties.find())
    
# Add a new city and then redirect to index
@app.route('/insert_city', methods=['POST'])
def insert_city():
    cities = mongo.db.cities
    city_info = {
        'city_name':request.form.get('city_name').capitalize(),
        'city_country':request.form.get('city_country').capitalize(),
        'city_population': request.form.get('city_population'),
        'city_description': request.form.get('city_description').capitalize(),
        'city_must_see': request.form.getlist('city_must_see').capitalize(),
        'city_category': request.form.getlist('city_category').capitalize(),
        'city_tips': request.form.get('city_tips').capitalize(),
        'city_author':request.form.get('city_author'),
        'city_image':request.form.get('city_image'),
        'favorite' :[
                    {'overall_favorite': 0.0,
                    'total_favorite': 0,
                    'no_of_favorite':0
                    }
                ],
        'added_time' : ctime()
    }
    cities.insert_one(city_info)
    return redirect(url_for('index'))
    
# Display all the City web page
@app.route('/city_page/<city_id>')
def city_page(city_id):
    return render_template("city.html", 
         cities = mongo.db.cities.find_one({'_id': ObjectId(city_id)}))
           
#Display all the cities listed 
@app.route('/get_cities')
def get_cities():
    return render_template("cities_listed.html", 
                           cities = mongo.db.cities.find())
    
# Get the city data from the city id
@app.route('/edit_city/<city_id>')
def edit_city(city_id):
    the_city =  mongo.db.cities.find_one({"_id": ObjectId(city_id)})
    with open('data/countries.json') as json_file:
         all_cities  = json.loads(json_file.read())
    return render_template('editcity.html', city=the_city,
                            country=all_cities)
    
@app.route('/update_city/<city_id>', methods=['POST'])
def update_city(city_id):
    cities = mongo.db.cities
    with open('data/countries.json') as json_file:
        json_file = json.loads(json_file.read())
    cities.update( {'_id': ObjectId(city_id)},
    {
        'city_name':request.form.get('city_name').capitalize(),
        'city_country':request.form.get('city_country').capitalize(),
        'city_population': request.form.get('city_population'),
        'city_description': request.form.get('city_description').capitalize(),
        'city_must_see': request.form.getlist('city_must_see').capitalize(),
        'city_category': request.form.getlist('city_category').capitalize(),
        'city_tips': request.form.get('city_tips').capitalize(),
        'city_image':request.form.get('city_image')
    })
    return redirect(url_for('index'))


# Delete city - to add an if statement before proceed with javascript
@app.route('/delete_city/<city_id>')
def delete_city(city_id):
    mongo.db.cities.remove({'_id': ObjectId(city_id)})
    return redirect(url_for('index'))


# ........................... Account details 

# SignUp form
@app.route('/signup')
def signup():
   return render_template ('signuppage.html', cities = mongo.db.cities.find())

# Get new user details and send them to MongoDB giving to all the users the right of user
@app.route('/get_user_data', methods=["POST"])
def get_user_data():
    user = mongo.db.user
    new_user = {
        'username':request.form.get('username').lower(),
        'email':request.form.get('email').lower(),
        'password':request.form.get('password'),
        'right': 'user'
    }
    user.insert_one(new_user)
    return redirect(url_for('index'))
    
# Get new user details and send them to MongoDB giving to all the users the right of user
@app.route('/login')
def login():
    return render_template ('login.html')
    

#Permitt the server to run the web app
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get("PORT")),
            debug=True)
