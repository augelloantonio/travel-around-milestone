import os
import json

#~~~~~~~~~~~~~~~~~~Testing if the json file is imported~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

with open('data/countries.json') as json_file:
    json_file = json.loads(json_file.read())
    for name in json_file:
        print (name['name'])
        

    

