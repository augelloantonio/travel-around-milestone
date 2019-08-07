#~~~~~~~~~~~~~~~~~~Importing necessary modules~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

import os
import json, pymongo
from flask import Flask, render_template, redirect, request, url_for, session, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 
from time import ctime
from werkzeug.security import generate_password_hash, check_password_hash


#~~~~~~~~~~~~~~~~~~Inizialize Flask and connect to MongoDB~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'travel_around'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')

app.secret_key = os.getenv('SECRET', 'randomstring123')

mongo = PyMongo(app)

#~~~~~~~~~~~~~~~~~~#Set as homepage my index.html~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
@app.route('/')
def index():
    #open coutries.json 
    with open('data/countries.json') as json_file_country:
        json_file_country = json.loads(json_file_country.read())
    #open region.json
    with open('data/region.json') as json_file_region:
        json_file_region = json.loads(json_file_region.read())
        
    username=session.get('username')
        
    return render_template("index.html", cities=mongo.db.cities.find().sort('added_time', pymongo.DESCENDING), 
                            cities_carousel=mongo.db.cities.find(), 
                            country=json_file_country, regions=json_file_region, user=mongo.db.user.find())


#~~~~~~~~~ CRUD - Create a new city, Read New city, Update existing city, Delete existing City ~~~~~~~~#
# Create city WebPage
@app.route('/add_city')
def add_city():
    country=[]
    #open coutries.json 
    with open('data/countries.json') as json_file_country:
        json_file_country = json.loads(json_file_country.read())
    #open region.json
    with open('data/region.json') as json_file_region:
        json_file_region = json.loads(json_file_region.read())
        
        return render_template('addcity.html', country=json_file_country, regions=json_file_region,
        city=mongo.db.cieties.find(), user=mongo.db.user.find())
        
# Create city function
@app.route('/insert_city', methods=['POST'])
def insert_city():
    cities = mongo.db.cities
    city_info = {
        'city_name':request.form.get('city_name').capitalize(),
        'city_country':request.form.get('city_country').capitalize(),
        'city_region':request.form.get('city_region').capitalize(),
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
    
# Get the city data from the city id
@app.route('/edit_city/<city_id>')
def edit_city(city_id):
    the_city =  mongo.db.cities.find_one({"_id": ObjectId(city_id)})
#open countries.json
    with open('data/countries.json') as json_file:
         all_cities  = json.loads(json_file.read())
#open region.json
    with open('data/region.json') as json_file_region:
        json_file_region = json.loads(json_file_region.read())     
    
    return render_template('editcity.html', city=the_city,
                            country=all_cities, regions=json_file_region, user=mongo.db.user.find())
    
@app.route('/update_city/<city_id>', methods=['POST'])
def update_city(city_id):
    cities = mongo.db.cities
#open countries.json
    with open('data/countries.json') as json_file:
        json_file = json.loads(json_file.read())
#open region.json
    with open('data/region.json') as json_file_region:
        json_file_region = json.loads(json_file_region.read())    
    cities.update( {'_id': ObjectId(city_id)},
    {
        'city_name':request.form.get('city_name').capitalize(),
        'city_country':request.form.get('city_country').capitalize(),
        'city_region':request.form.get('city_region').capitalize(),
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


#Display the City webpage 
@app.route('/city_page/<city_id>')
def city_page(city_id):
    return render_template("city.html", 
         cities = mongo.db.cities.find_one({'_id': ObjectId(city_id)}))
           
           
#~~~~~~~~~~~~~~~~~~ Display all the City webpage ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
@app.route('/get_cities')
def get_cities():
    return render_template("cities_listed.html", 
                           cities = mongo.db.cities.find())
    



#~~~~~~~~~~~~~~~~~~ Register / Log In/ Account section ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

# register form
@app.route('/register')
def register():
   return render_template ('signuppage.html')
   
# register form
@app.route('/login_page')
def login_page():
   return render_template ('login.html')


# Get new user details and send them to MongoDB giving to all the users the right of user
@app.route('/get_user_data', methods=['POST'])
def get_user_data():
    username = request.form.get('username').lower()
    password = generate_password_hash(request.form.get('password'))
    email = request.form.get('email').lower()
    session['username'] = username
    new_user = mongo.db.user.find_one({'username' : username})
    
    if new_user is None:
        mongo.db.user.insert_one({
            'username': username,
            'password': password,
            'email': email,
            'recipes_rated':[]
        })
        session['logged_in'] = True
        flash('Your User has been creates, please Log In now')
        return redirect(url_for('login_page'))
    else:
        session['logged_in'] = False
        flash('Username already exists, please try again.')
        return redirect(url_for('user_page'))
   

#Check if user already logged in 
@app.route('/user_logged')
def user_logged():
    if not session.get('logged_in'):
        return render_template('login.html')
        flash("Please, Log In")
    else:
        return redirect(url_for('user_page'))
    
@app.route('/login',  methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    username = request.form.get('username')
    session['username'] = username

    session.permanent = True
    user = mongo.db.user.find_one({'email' : email})
    
    if not user:
        session['logged_in'] = False
        flash('Username not in the database, try again.')
        return login_page()
    elif not check_password_hash(user['password'],password):
        session['logged_in'] = False
        flash('Incorrect Password, please try again.')
        return login_page()   
    else:
        session['logged_in'] = True
        flash('Welcome ' + user['username'])
        return redirect(url_for('user_page'))


# User Page
@app.route('/user_page')
def user_page():
    username=session.get('username')
    return render_template ('user.html', user=mongo.db.user.find())


#Permitt the server to run the web app
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get("PORT")),
            debug=True)
