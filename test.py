import os
import json
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 

#~~~~~~~~~~~~~~~~~~Testing if the json file is imported~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

with open('data/countries.json') as json_file:
    json_file = json.loads(json_file.read())
    for name in json_file:
        print (name['name'])
        


