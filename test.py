import os
import json
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 
from time import ctime

#Inizialize Flask
app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'travel_around'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')

mongo = PyMongo(app)

#~~~~~~~~~~~~~~~~~~Testing if mongoDB database is imported~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
cities = mongo.db.cities.find({'city_name': 'berlin'})
for item in cities:
    print (item)
    print()
 
#~~~~~~~~~~~~~~~~~~Testing if the json file is imported~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

with open('data/countries.json') as json_file:
    json_file = json.loads(json_file.read())
    for name in json_file:
        if name['name'].startswith("Au"):
            print (name['name'])
            print ('')


#~~~~~~~~~~~~~~~~~~Testing if the date is correctly setted~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

time = ctime()
print ("actual time is: " + time)
print('')

#~~~~~~~~~~~~~~~~~~Testing the links ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

