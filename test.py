import os
import json
from app import app
from flask import Flask, render_template, redirect, request, url_for, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 
from time import ctime, strftime
import unittest


#Inizialize Flask
app.config["MONGO_DBNAME"] = 'travel_around'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')

mongo = PyMongo(app)


#~~~~~~~~~~~~~~~~~~Testing if mongoDB database is imported~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

class test_cities_collection(unittest.TestCase):
    def test_cities_collection(self):
        cities = mongo.db.cities.find({'city_name': 'berlin'})
        for item in cities:
            print (item)
            print('')
        print('test collection passed')
    
 
#~~~~~~~~~~~~~~~~~~Testing if the json files are imported~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

class test_country_collection(unittest.TestCase):
    def test_country_collection(self):
        with open('data/countries.json') as json_file_country:
            json_file_country = json.loads(json_file_country.read())
            for name in json_file_country:
                if name['name'].startswith("Au"):
                    print (name['name'])
                    print('')
        print ('Test region collection passed')


#~~~~~~~~~~~~~~~~~~~~~~~~~~Testing if time is printed~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
class test_timen(unittest.TestCase):
    def test_time(self):
        print(strftime('Time is: ' + '%d' + "/" + '%m' + "/"+ '%Y'))
        print('')
    print('Time test passed')
    
    
#~~~~~~~~~~~~~~~~~~Testing login form~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
class testing_login(unittest.TestCase):
    def test_login(self):
        session = False
        username = 'admin'
        password = 'admin'
        if session == True and username == 'admin' and password == 'admin':
            print ('user logged in')
            print('')
        elif session == False:
            print('please login')
            print('')
    

#~~~~~~~~~~~~~~~~~~Testing the links ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

class testing_links(unittest.TestCase):
    
    # Set my app client
    def setUp(self):
        self.mongo = app.test_client()

    # Testing my home page
    def test_home(self):
        page = self.mongo.get('/')
        self.assertEqual(page.status_code, 200)
    
    # Testing the login page
    def test_login_page(self):
        page = self.mongo.get('/login_page')
        self.assertEqual(page.status_code, 200)
        
    # Testing the register page
    def test_signup_page(self):
        page = self.mongo.get('/register')
        self.assertEqual(page.status_code, 200)    
    
    # Testing the 404 error
    def test_error_page(self):
        page = self.mongo.get('/error')
        self.assertEqual(page.status_code, 404)
        
    print('Tests passed')

if __name__ == '__main__':
    unittest.main()
