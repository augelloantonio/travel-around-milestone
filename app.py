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

app.secret_key = 'randomstring123'

mongo = PyMongo(app)

#~~~~~~~~~~~~~~~~~~#Set as homepage my index.html~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
@app.route('/')
@app.route('/index')
def index():
    #open coutries.json 
    with open('data/countries.json') as json_file_country:
        json_file_country = json.loads(json_file_country.read())
    #open region.json
    with open('data/region.json') as json_file_region:
        json_file_region = json.loads(json_file_region.read())
        
        username=session.get('username')
        user = mongo.db.user.find_one({'username' : username})
        
    return render_template("index.html", cities=mongo.db.cities.find().sort('added_time', pymongo.DESCENDING), 
                            cities_carousel= mongo.db.cities.find(), city=mongo.db.cities.find(), 
                            city_named= mongo.db.cities.find(), city_2=mongo.db.cities.find(),
                            city_3=mongo.db.cities.find(), city_4=mongo.db.cities.find(),
                            city_5=mongo.db.cities.find(),
                            country=json_file_country, regions=json_file_region, user=mongo.db.user.find()
                            )

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
    cities = mongo.db.cities.find()
    
    return render_template('addcity.html', country=json_file_country, regions=json_file_region,
    city=mongo.db.cieties.find(), user=mongo.db.user.find(), count_cities = cities.count())


# Create city function
@app.route('/insert_city', methods=['POST'])
def insert_city():
    username=session.get('username')
    user = mongo.db.user.find_one({'username' : username})
    cities = mongo.db.cities
    city_info = {
        'city_name':request.form.get('city_name').lower(),
        'city_country':request.form.get('city_country'),
        'city_region':request.form.get('city_region'),
        'city_population': request.form.get('city_population'),
        'city_language': request.form.get('city_language'),
        'city_description': request.form.getlist('city_description'),
        'city_must_see': request.form.getlist('city_must_see'),
        'city_category': request.form.getlist('city_category'),
        'city_tips': request.form.getlist('city_tips'),
        'city_author': username,
        'city_image':request.form.get('city_image'),
        'added_time' : ctime()
    }
    cities.insert_one(city_info)
    
    #Add city to user log 
    city_added = mongo.db.user['number_city_added']
    tot_cities_added = city_added +1
    mongo.db.user.update({"username": username},
                {'$addToSet': 
                {'number_city_added' : tot_cities_added,
                 'name_city_added': request.form.get('city_name')
                }}) 
    
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
                            country=all_cities, regions=json_file_region, user=mongo.db.user)
                            
    
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
        'city_name':request.form.get('city_name').lower(),
        'city_country':request.form.get('city_country'),
        'city_region':request.form.get('city_region'),
        'city_population': request.form.get('city_population'),
        'city_language': request.form.get('city_language'),
        'city_description': request.form.get('city_description'),
        'city_must_see': request.form.getlist('city_must_see'),
        'city_category': request.form.getlist('city_category'),
        'city_tips': request.form.getlist('city_tips'),
        'city_image': request.form.get('city_image'),
        'city_author': request.form.get('city_author')
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
    the_city =  mongo.db.cities.find_one({"_id": ObjectId(city_id)})
    return render_template("city.html", 
         cities = mongo.db.cities.find_one({'_id': ObjectId(city_id)}), city=the_city,
                          user=mongo.db.user.find(), cities_carousel=mongo.db.cities.find_one({'_id': ObjectId(city_id)}),
                          city_must_see=mongo.db.cities.find())


@app.route('/cities_for_regions/<city_region>')
def cities_for_regions(city_region):
        with open('data/region.json') as json_file_region:
            json_file_region = json.loads(json_file_region.read()) 
            return render_template ("cities_for_regions.html", 
                regions = json_file_region, cities = mongo.db.cities.find().sort('city_name'),
                city_region=city_region)
                

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

#Check if user already logged in 
@app.route('/user_logged')
def user_logged():
    if not session.get('logged_in'):
        flash("Please, Log In")
        return render_template('login.html')
    else:
        return redirect(url_for('user_page'))

@app.route('/get_user_data', methods=['POST'])
def get_user_data():
    username = request.form['username'].lower()
    password = generate_password_hash(request.form['password'])
    email = request.form['email'].lower()
    city_author = request.form['username'].lower()
    right = 'user'
    
    session['username'] = username
    session.permanent = True

    new_user = mongo.db.user.find_one({'username' : username})
    
    if new_user is None:
        mongo.db.user.insert_one({
            'username': username,
            'password': password,
            'email': email,
            'city_author': city_author,
            'right': right,
            'number_city_added': []
        })
        session['logged_in'] = True
        flash('Your User has been creates, please Log In now')
        return render_template('login.html')
    else:
        session['logged_in'] = False
        flash('Username already exists, please try again.')
        return redirect(url_for('register'))
        
        
@app.route('/login',  methods=['POST', 'GET'])
def login():
    username = request.form['username'].lower()
    password = request.form['password']
    
    session['username'] = username
    session.permanent = True
    user = mongo.db.user.find_one({'username' : username})

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
        return render_template('user.html', user=mongo.db.user.find(), 
        city_author=user['username'], cities=mongo.db.cities.find())
    
#Log Out
@app.route('/logout')
def logout():
    session['logged_in'] = False
    return index()
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~Personal pages~~~~~~~~~~~~~~~~~~~~~~#
# User Personal Page
@app.route('/user_page')
def user_page():
    username=session.get('username')
    user = mongo.db.user.find_one({'username': username})
    cities = mongo.db.cities.find()
    
    if session['logged_in'] == False and username is None:
        return login_page()
    else:
        return render_template('user.html', user=mongo.db.user.find(),
        cities = mongo.db.cities.find().sort('added_time', pymongo.DESCENDING), tot_cities=cities.count())
        

#Display the City webpage 
@app.route('/userpublicpage/<user_id>')
def userpublicpage(user_id):
    the_user =  mongo.db.user.find_one({"_id": ObjectId(user_id)})
    return render_template("userpage.html", username = mongo.db.user.find_one({"_id": ObjectId(user_id)}),
                          cities = mongo.db.cities.find(), user = the_user)
    

#~~~~~~~~~~~~~~~~~~~~~~~~ Admin Settings Page ~~~~~~~~~~~~~~~~~~~~~~~~~#
@app.route('/admin_settings')
def admin_settings():
    return render_template('admin_settings.html', users = mongo.db.user.find())

#Make a change user right page
@app.route('/user_rights/<user_id>')
def user_rights(user_id):
    the_user = mongo.db.user.find_one({'_id': ObjectId(user_id)})
    return render_template('user_right.html', user = the_user, users = mongo.db.user.find())
    
# Change the user right and update info in mongodb
@app.route('/edit_user_rights/<user_id>', methods=['POST'])
def edit_user_rights(user_id):
    users = mongo.db.user.find()
    the_user = mongo.db.user.find_one({'_id': ObjectId(user_id)})
    users.update( {'_id': ObjectId(user_id)},
    {
        'right': request.form.get('user_right'),
    })
    return redirect(url_for('admin_settings'))
    

#~~~~~~~~~~~~~~~~~~~~~~~~ Search Form ~~~~~~~~~~~~~~~~~~~~~~~~~#
# Get the city
@app.route('/search_city', methods=['POST'])
def search_city():
    return redirect(url_for('search_a_city', search_city = request.form.get('search_city')))

@app.route('/search_a_city/<search_city>', methods=['GET'])
def search_a_city(search_city):

    mongo.db.cities.create_index([('city_name', 'text')])        
    
    #Count the number of cities in the Database
    all_cities = mongo.db.cities.find({'$text': {'$search': search_city}}).sort([('date_time', pymongo.DESCENDING), ('_id', pymongo.ASCENDING)])
    count_cities = all_cities.count()
    
    city_page = mongo.db.cities.find({'$text': {'$search': search_city}}).sort([("date_time", pymongo.DESCENDING), 
                    ("_id", pymongo.ASCENDING)])
                    
    return render_template('search_city.html', search_city=search_city.lower(), cities=mongo.db.cities.find(),
        search_results = city_page.sort('date_time',pymongo.DESCENDING), count_cities=count_cities, )
    
    
#Permitt the server to run the web app
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get("PORT")),
            debug=False)
