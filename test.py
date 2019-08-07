import os
import json
from app import app
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 
from time import ctime
import unittest


#Inizialize Flask
app.config["MONGO_DBNAME"] = 'travel_around'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')

mongo = PyMongo(app)


#~~~~~~~~~~~~~~~~~~Testing if mongoDB database is imported~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

cities = mongo.db.cities.find({'city_name': 'berlin'})
for item in cities:
    print (item)
    print()
    
 
#~~~~~~~~~~~~~~~~~~Testing if the json files are imported~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#


with open('data/countries.json') as json_file_country:
    json_file_country = json.loads(json_file_country.read())
    for name in json_file_country:
        if name['name'].startswith("Au"):
            print (name['name'])
            print ('')

#testing region directory
with open('data/region.json') as json_file_region:
    json_file_region = json.loads(json_file_region.read())
    for region in json_file_region:
        if region['region_name']:
            print(region['region_name'])



#~~~~~~~~~~~~~~~~~~Testing if the date is correctly setted~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

time = ctime()
print ("actual time is: " + time)
print('')

#~~~~~~~~~~~~~~~~~~Testing if the date is correctly setted~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#


#~~~~~~~~~~~~~~~~~~Testing the links ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
"""
class testing_links(unittest.TestCase):
    
    def setUp(self):
        self.mongo = app.test_client()

    def test_home(self):
        page = self.mongo.get('/')
        self.assertEqual(page.status_code, 202)

    def test_add_city(self):
        response = self.mongo.get('/add_city')
        self.assertEqual(response.status_code, 200)
        
"""
if __name__ == '__main__':
    unittest.main()
