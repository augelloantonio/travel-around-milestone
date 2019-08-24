#~~~~~~~~~~~~~~~~~~Importing necessary modules~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

import os
import json, pymongo, random
from flask import Flask, render_template, redirect, request, url_for, session, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 
from time import ctime, strftime
from werkzeug.security import generate_password_hash, check_password_hash
from bson import json_util
from bson.json_util import dumps


#~~~~~~~~~~~~~~~~~~Inizialize Flask and connect to MongoDB~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'travel_around'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')

app.secret_key = os.getenv('SECRET', 'randomstring123')

mongo = PyMongo(app)

# Variable
cities = mongo.db.cities
regions = mongo.db.regions
users = mongo.db.user

#~~~~~~~~~~~~~~~~~~#Set as homepage my index.html~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
@app.route('/')
@app.route('/index')
def index():
    username=session.get('username')
    user_logged = users.find_one({'username' : username})
    cities_preferred_count = cities.find({'cities_preferred_by': 1}).count()


# Set limit 16 to prevent showing more than 8 elements for region
    return render_template("index.html", cities=cities.find().sort('added_time', pymongo.DESCENDING).limit(16),
                            cities_carousel= cities.find().sort('city_name').limit(6),
                            city=cities.find().sort('added_time', pymongo.DESCENDING).limit(16), 
                            cities_1= cities.find().sort('added_time', pymongo.DESCENDING).limit(16), 
                            cities_2=cities.find().sort('added_time', pymongo.DESCENDING).limit(16),
                            cities_3=cities.find().sort('added_time', pymongo.DESCENDING).limit(16), 
                            cities_4=cities.find().sort('added_time', pymongo.DESCENDING).limit(16),
                            cities_5=cities.find().sort('added_time', pymongo.DESCENDING).limit(16), 
                            regions = regions.find(),
                            user_logged=user_logged)

#~~~~~~~~~ CRUD - Create a new city, Read New city, Update existing city, Delete existing City ~~~~~~~~#
# Create city WebPage
@app.route('/add_city')
def add_city():
    country=[]
    #open coutries.json 
    with open('data/countries.json') as json_file_country:
        json_file_country = json.loads(json_file_country.read())
    username=session.get('username')
    user_logged = users.find_one({'username' : username})
    
    if not session.get('logged_in'): 
        return redirect(url_for('login_page'))
    else:
        return render_template('addcity.html', country=json_file_country, regions=regions.find(),
        city=cities.find(), user=users.find(), count_cities = cities.count(),
        user_logged=user_logged)


# Create city function
@app.route('/insert_city', methods=['POST'])
def insert_city():
    username=session.get('username')
    user_logged = users.find_one({'username' : username})
    city_info = {
        'city_name':request.form.get('city_name').lower(),
        'city_country':request.form.get('city_country'),
        'city_region':request.form.get('city_region'),
        'city_population': request.form.get('city_population'),
        'city_language': request.form.get('city_language'),
        'city_description': request.form.get('city_description'),
        'city_must_see': request.form.getlist('city_must_see'),
        'city_category': request.form.get('city_category'),
        'city_tips': request.form.getlist('city_tips'),
        'city_to_avoid': request.form.getlist('city_to_avoid'),
        'city_author': username,
        'city_image':request.form.get('city_image'),
        'added_time' : strftime('%d' + "/" + '%m' + "/"+ '%Y')
    }
    cities.insert_one(city_info)
    
    # Add to the user the list of cities made
    users.update({"username": username},
            {'$addToSet': 
            {'cities_made' : request.form.get('city_name').lower()}})
            
    # Add to region the list of cities in that region
    region_name = request.form.get('city_region')
    regions.update({"region_name": region_name},
            {'$addToSet': 
            {'cities_in _region' : request.form.get('city_name')}})
    
    return redirect(url_for('user_page'))
    

# Get the city data from the city id
@app.route('/edit_city/<city_id>')
def edit_city(city_id):
    the_city =  cities.find_one({"_id": ObjectId(city_id)})
#open countries.json
    with open('data/countries.json') as json_file:
         all_cities  = json.loads(json_file.read())
    username=session.get('username')
    user_logged = users.find_one({'username' : username})
    
    if not session.get('logged_in'): 
        return redirect(url_for('login_page'))
    else:
        return render_template('editcity.html', city=the_city,
            country=all_cities, regions=regions.find(), user=users, user_logged=user_logged)
                            
    
@app.route('/update_city/<city_id>', methods=['POST'])
def update_city(city_id):
#open countries.json
    with open('data/countries.json') as json_file:
        json_file = json.loads(json_file.read())
    cities.update( {'_id': ObjectId(city_id)},
    {"$set":
    {
        'city_name':request.form.get('city_name').lower(),
        'city_country':request.form.get('city_country'),
        'city_region':request.form.get('city_region'),
        'city_population': request.form.get('city_population'),
        'city_language': request.form.get('city_language'),
        'city_description': request.form.get('city_description'),
        'city_must_see': request.form.getlist('city_must_see'),
        'city_category': request.form.get('city_category'),
        'city_tips': request.form.getlist('city_tips'),
        'city_to_avoid': request.form.getlist('city_to_avoid'),
        'city_image': request.form.get('city_image'),
    }})
    return redirect(url_for('index'))


# Delete city - to add an if statement before proceed with javascript
@app.route('/delete_city/<city_name>/<city_id>')
def delete_city(city_name, city_id):
    username=session.get('username')
    user_logged = users.find_one({'username' : username})
    cities.remove({'_id': ObjectId(city_id)})
    the_city = cities.find_one({'city_name': city_name})
    users.update({"username": username},
            {'$pull': 
            {'cities_made' : city_name}})
    return redirect(url_for('user_page'))


#Display the City webpage 
@app.route('/city_page/<city_id>')
def city_page(city_id):
    the_city =  cities.find_one({"_id": ObjectId(city_id)})
    username=session.get('username')
    user_logged = users.find_one({'username' : username})
    return render_template("city.html", cities = cities.find_one({'_id': ObjectId(city_id)}),
    city=the_city, user=users.find(), cities_carousel=cities.find_one({'_id': ObjectId(city_id)}),
    city_must_see=cities.find(), user_logged=user_logged)


@app.route('/cities_for_regions/<city_region>')
def cities_for_regions(city_region):

            username=session.get('username')
            user_logged = users.find_one({'username' : username})
            return render_template ("cities_for_regions.html", 
                regions=regions.find(), cities = cities.find().sort('city_name'),
                city_region=city_region, user_logged=user_logged, city=cities.find())
                

#~~~~~~~~~~~~~~~~~~ Register / Log In/ Account section ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

# register page form
@app.route('/register')
def register():
    if not session.get('logged_in'):        
        return render_template ('signuppage.html')
    else:
        return redirect(url_for('user_page'))
   
   
# login page form
@app.route('/login_page')
def login_page():
    if not session.get('logged_in'): 
        return render_template ('login.html')
    else: 
        return redirect(url_for('user_page'))

# Get new user details and send them to MongoDB giving to all the users the right of user
@app.route('/get_user_data', methods=['POST'])
def get_user_data():
    username = request.form['username'].lower()
    password = generate_password_hash(request.form['password'])
    email = request.form['email'].lower()
    city_author = request.form['username'].lower()
    right = 'user'
    
    session['username'] = username
    session.permanent = True

    new_user = users.find_one({'username' : username})
    new_email = users.find_one({'email': email})
    
    if new_email is not None:
        session['logged_in'] = False
        flash('An user with same email exist already, please try again.')
        return redirect(url_for('register'))
    if new_user is None:
        users.insert_one({
            'username': username,
            'password': password,
            'email': email,
            'city_author': city_author,
            'right': right,
            'number_city_added': []
        })
        session['logged_in'] = True
        flash('Welcome aboard ' + username)
        return redirect(url_for('user_page'))
    else:
        session['logged_in'] = False
        flash('An user with same username exist already, please try again.')
        return redirect(url_for('register'))
        
        
@app.route('/login',  methods=['POST', 'GET'])
def login():
    username = request.form['username'].lower()
    password = request.form['password']
    session['username'] = username
    session.permanent = True
    user = users.find_one({'username' : username})

    if not user:
        session['logged_in'] = False
        flash('Username not in the database, try again.')
        return login_page()
    elif not check_password_hash(user['password'],password):
        session['logged_in'] = False
        flash('Incorrect Password, please try again.')
        return redirect(url_for('login_page'))
    else:
        session['logged_in'] = True
        user_logged = users.find_one({'username' : username})
        return redirect(url_for('user_page', user=users.find(), 
        city_author=user['username'], cities=cities.find(), user_logged=user_logged))
    
#Log Out
@app.route('/logout')
def logout():
    session.clear()
    session['logged_in'] = False
    return redirect(url_for('index'))
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Delete User ~~~~~~~~~~~~~~~~~~~~~~~~~~~#
@app.route('/delete_user/<user_id>')
def delete_user(user_id):
    session['logged_in'] == False
    username=session.get('username')
    user_logged = users.find_one({'username' : username})
    users.remove({'_id': ObjectId(user_id)})
    if user_logged['right'] == 'admin':
        return redirect(url_for('index'))
    else:
        return redirect(url_for('logout'))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~Personal pages~~~~~~~~~~~~~~~~~~~~~~#
# User Personal Page
@app.route('/user_page')
def user_page():
    username=session.get('username')
    user_logged = users.find_one({'username' : username})
    if not session.get('logged_in'): 
        return redirect(url_for('login_page'))
    else:
        return render_template('user.html', user=users.find(),
        cities = cities.find().sort('added_time', pymongo.DESCENDING), tot_cities=cities.count(),
        user_logged=user_logged, city=cities.find(), city_name = users.find(), 
        cities_visited=cities.find(), cities_to_visit=cities.find(), 
        cities_preferite=cities.find())


#Display the City webpage 
@app.route('/userpublicpage/<user_id>')
def userpublicpage(user_id):
    the_user =  users.find_one({"_id": ObjectId(user_id)})
    username=session.get('username')
    user_logged = users.find_one({'username' : username})
    if not session.get('logged_in'): 
        return redirect(url_for('login_page'))
    else:
        return render_template("userpage.html", username = users.find_one({"_id": ObjectId(user_id)}),
                          cities = cities.find(), user = the_user, user_logged=user_logged,
                          city=cities.find(), city_name = users.find(), 
                          cities_visited=cities.find(), cities_to_visit=cities.find(), 
                          cities_preferite=cities.find())


#~~~~~~~~~~~~~~~~~~~~~~~~ Admin Settings Page ~~~~~~~~~~~~~~~~~~~~~~~~~#
@app.route('/admin_settings')
def admin_settings():
    username=session.get('username')
    user_logged = users.find_one({'username' : username})
    if not session.get('logged_in'): 
        return redirect(url_for('login_page'))
    else:
        return render_template('admin_settings.html', users = users.find(), user_logged=user_logged)

#Make a change user right page
@app.route('/user_rights/<user_id>')
def user_rights(user_id):
    username=session.get('username')
    user_logged = users.find_one({'username' : username})
    the_user = users.find_one({'_id': ObjectId(user_id)})
    if not session.get('logged_in'): 
        return redirect(url_for('login_page'))
    elif user_logged['right'] != 'admin':
        return redirect(url_for('user_page'))
    else:
        return render_template('user_right.html', user = the_user, users = users.find(),
        user_logged=user_logged)


# Change the user right and update info in mongodb
@app.route('/edit_user_rights/<user_id>', methods=['POST'])
def edit_user_rights(user_id):
    username=session.get('username')
    user_logged = users.find_one({'username' : username})
    the_user = users.find_one({'_id': ObjectId(user_id)})
    users.update({'_id': ObjectId(user_id)},
    {"$set":
        {'right': request.form.get('user_right'),
        }
    })
    return redirect(url_for('admin_settings', user= the_user, user_logged=user_logged))
    

#~~~~~~~~~~~~~~~~~~~~~~~~ Search Form ~~~~~~~~~~~~~~~~~~~~~~~~~#
# Get the city
@app.route('/search_city', methods=['POST'])
def search_city():
    return redirect(url_for('search_a_city', search_city = request.form.get('search_city')))


@app.route('/search_a_city/<search_city>', methods=['GET'])
def search_a_city(search_city):

    cities.create_index([('city_name', 'text')])  
    username=session.get('username')
    user_logged = users.find_one({'username' : username})
    
    #Count the number of cities in the Database
    all_cities = cities.find({'$text': {'$search': search_city}}).sort([('date_time', pymongo.DESCENDING), ('_id', pymongo.ASCENDING)])
    count_cities = all_cities.count()
    
    city_page = cities.find({'$text': {'$search': search_city}}).sort([("date_time", pymongo.DESCENDING), 
                    ("_id", pymongo.ASCENDING)])
                    
    return render_template('search_city.html', search_city=search_city.lower(), cities=cities.find(),
        search_results = city_page.sort('date_time',pymongo.DESCENDING), count_cities=count_cities, user_logged=user_logged)


#~~~~~~~~~~~~~~~~~~~~~~~~To visit list~~~~~~~~~~~~~~~~~~~~~~#
@app.route('/add_to_visit/<city_name>/<city_id>')
def add_to_visit(city_name, city_id):
    username=session.get('username')
    user_logged = users.find_one({'username' : username})
    user = users.find_one({'username' : username}) 
    city = cities.find_one({"_id": ObjectId(city_id)})

    if not session.get('logged_in'): 
        return redirect(url_for('permitt_required'))
    else:
        users.update({"username": username},
            {'$addToSet': 
            {'city_to_visit' : city_name}})
        cities.update({"_id": ObjectId(city_id)},
            {'$addToSet': 
            {'city_to_visit_by' : username}})
        return redirect(url_for('index', city_name = city_name, city_id=city_id))


@app.route('/remove_to_visit/<city_name>/<city_id>')
def remove_to_visit(city_name, city_id):
    username=session.get('username')
    user_logged = users.find_one({'username' : username})
    user = users.find_one({'username' : username}) 
    city = cities.find_one({"_id": ObjectId(city_id)})
    users.update({"username": username},
            {'$pull': 
            {'city_to_visit' : city_name}})
    cities.update({"_id": ObjectId(city_id)},
            {'$pull': 
            {'city_to_visit_by' : username}})
    return redirect(url_for('user_page', city_name = city_name, city=cities.find(), city_id=city_id))
    
    
#~~~~~~~~~~~~~~~~~~~~~~~~Visited list~~~~~~~~~~~~~~~~~~~~~~#

@app.route('/add_to_visited/<city_name>/<city_id>')
def add_to_visited(city_name, city_id):
    username=session.get('username')
    user_logged = users.find_one({'username' : username})
    user = users.find_one({'username' : username}) 
    the_city = cities.find_one({'city_name': city_name})
    city = cities.find_one({"_id": ObjectId(city_id)})
    
    if not session.get('logged_in'): 
        return redirect(url_for('permitt_required'))
    else:
        users.update({"username": username},
            {'$addToSet': 
            {'city_visited' : city_name}})
        cities.update({"_id": ObjectId(city_id)},
            {'$addToSet': 
            {'city_visited_by' : username}})
        return redirect(url_for('index', city_name = city_name, city_id=city_id))


@app.route('/remove_visited/<city_name>/<city_id>')
def remove_visited(city_name, city_id):
    username=session.get('username')
    user_logged = users.find_one({'username' : username})
    user = users.find_one({'username' : username}) 
    city = cities.find_one({"_id": ObjectId(city_id)})
    
    users.update({"username": username},
            {'$pull': 
            {'city_visited' : city_name}})
    cities.update({"_id": ObjectId(city_id)},
            {'$pull': 
            {'city_visited_by' : username}})
    return redirect(url_for('user_page', city_name = city_name, city=cities.find(), city_id=city_id))


#~~~~~~~~~~~~~~~~~~~~~~~~Preferite list~~~~~~~~~~~~~~~~~~~~~~#

@app.route('/add_to_preferite/<city_name>/<city_id>')
def add_to_preferite(city_name, city_id):
    username=session.get('username')
    user_logged = users.find_one({'username' : username})
    user = users.find_one({'username' : username}) 
    the_city = cities.find_one({'city_name': city_name})
    city = cities.find_one({"_id": ObjectId(city_id)})

    if not session.get('logged_in'): 
        return redirect(url_for('permitt_required'))
    else:
        users.update({"username": username},
            {'$addToSet': 
            {'preferite_cities' : city_name}})
        cities.update({"_id": ObjectId(city_id)},
            {'$addToSet': 
            {'city_preferred_by' : username }
            })
    return redirect(url_for('index', city_name = city_name, city_id=city_id))



@app.route('/remove_preferite/<city_name>/<city_id>')
def remove_preferite(city_name, city_id):
    username=session.get('username')
    user_logged = users.find_one({'username' : username})
    user = users.find_one({'username' : username}) 
    city = cities.find_one({"_id": ObjectId(city_id)})

    users.update({"username": username},
            {'$pull': 
            {'preferite_cities' : city_name}})
    cities.update({"_id": ObjectId(city_id)},
            {'$pull': 
            {'city_preferred_by' : username}})
    return redirect(url_for('user_page', city_name = city_name, city=cities.find(),
    preferites=users.find(), city_id=city_id))


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~User List and Info~~~~~~~~~~~~~~~~~~~#
@app.route('/user_list')
def user_list():
    username=session.get('username')
    user_logged = users.find_one({'username' : username})
    if not session.get('logged_in'): 
        return redirect(url_for('login_page'))
    else:
        return render_template('users_registered.html', users = users.find(), user_logged=user_logged)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Permitt Page ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
@app.route('/permitt_required')
def permitt_required():
    username=session.get('username')
    user_logged = users.find_one({'username' : username})
    return render_template('permitt_required.html', user_logged=user_logged)


#~~~~~~~~~~~~~~~~~~~~~~~~~~Error Pages~~~~~~~~~~~~~~~~~~~~~~~#
@app.errorhandler(404)
def page_not_found(error):
    username=session.get('username')
    user_logged = users.find_one({'username' : username})
    return render_template('404.html', user_logged=user_logged), 404

@app.errorhandler(500)
def something_wrong(error):
    username=session.get('username')
    user_logged = users.find_one({'username' : username})
    return render_template('500.html', user_logged=user_logged), 500


#Permitt the server to run the web app
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get("PORT")),
            debug=True)
            
            
            

