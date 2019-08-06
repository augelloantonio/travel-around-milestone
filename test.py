import os
import app
import json
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 
from time import ctime
import unittest

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

class testing_links(unittest.TestCase):
    
    def setUp(self):
        self.mongo = app.test_client()

    def test_home(self):
        page = self.mongo.get('/')
        self.assertEqual(page.status_code, 202)

    def test_add_city(self):
        response = self.mongo.get('/add_city')
        self.assertEqual(response.status_code, 200)
        
        
if __name__ == '__main__':
    unittest.main()
