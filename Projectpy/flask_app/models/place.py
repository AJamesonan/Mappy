from flask_app.config.mysqlconnection import MySQLConnection, connectToMySQL

from flask import flash, session
from flask_app import app
from flask_app.models.user import User 
import re	

import requests
import os

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

db='map_dashboard'

class Place:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.city = data['city']
        self.state = data['state']
        self.street_address = data['street_address']
        self.zip = data['zip']
        self.place_id = data['place_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @staticmethod
    def place_is_valid(place):
        is_valid = True
        if place['name'] == "":
            flash('Give place name')
            is_valid = False
        if place['city'] == "":
            flash('Give place city information')
            is_valid = False
        if place['state'] == "":
            flash('select place state')
            is_valid = False
        if place['street_address'] == "":
            flash('please add address of place')
        if place['zip'] == "":
            flash('please add zip of place')
        return is_valid
        


    

    @classmethod
    def save_place(cls,data):
        data['place_id'] = Place.get_placeid(data)
        data['user_id'] = session['user_id']
        query = "INSERT INTO places (name, city, state, street_address, zip, place_id, user_id) VALUES (%(name)s, %(city)s,%(state)s, %(street_address)s, %(zip)s,  %(place_id)s, %(user_id)s);"
        connectToMySQL(db).query_db(query, data)
        return

    @classmethod
    def get_place_by_id(cls,data):
        query = 'SELECT * FROM places WHERE id = %(id)s'

        results = connectToMySQL(db).query_db(query, data)
        
        return cls(results[0])
    
    @classmethod
    def get_place_id_by_name(cls,name):
        data={
            'name':name
        }
        query = 'SELECT * FROM places WHERE name = %(name)s;'
        results = connectToMySQL(db).query_db(query, data)
        place_id= []
        for id in results:
            place_id.append(id)
        print(place_id)
        return results[0]['place_id']

    @classmethod
    def get_places(cls):
        data={
            "user_id": session['user_id']
        }
        query = 'SELECT * FROM places WHERE user_id = %(user_id)s ;'
        results =  connectToMySQL(db).query_db(query,data)
        list_places = []
        for row in results:
            current_place = cls(row)
            list_places.append(current_place)
        return list_places

    @classmethod
    def update_one(cls,data):
        query = 'UPDATE places SET name = %(name)s, city = %(city)s, state = %(state)s, street_address = %(street_address)s, zip = %(zip)s WHERE id = %(id)s;'
        return connectToMySQL(db).query_db(query,data)

    classmethod
    def delete_one(data):
        query = 'DELETE FROM places WHERE id = %(id)s;'
        return connectToMySQL(db).query_db(query,data)
    
    @classmethod
    def get_placeid(cls,place):
        api_request = requests.get("https://www.google.com/maps/api/geocode/json?address=" + 
                    place['street_address']+ " "+ place['city'] + " "+ place['state'] + " "+ place['zip'] +"&key="+ os.environ.get("FLASK_APP_API_KEY"))
        print(api_request)
        return api_request.json()['results'][0]['place_id']
    
    @classmethod
    def get_travel_times(cls):
        destination_id = []
        place_key = []
        places = Place.get_places()
        for place in places:
            current_place = place.__dict__
            current_place
            destination_id.append(current_place['place_id'])
            place_key.append(current_place['name'])
        destinations = '|place_id:'.join(destination_id)
        print(destinations)
        if 'origin' in session:  
            origin_id = session['origin']
            travel_time = {}
            uri = requests.get("https://maps.googleapis.com/maps/api/distancematrix/json?departure_time=now&destinations=place_id:" +destinations+ "&origins=place_id:"+origin_id+"&key="+ os.environ.get("FLASK_APP_API_KEY"))
            print('line - 138')
            # print( uri.json()['rows'][0]['elements'][0]['duration']['text'])
            elements_list = uri.json()['rows'][0]['elements']
            j =0
            for i in range(len(elements_list)):
                if 'duration' in elements_list[i]:
                    travel_time[place_key[j]] = elements_list[i]['duration']['text']
                    j= j + 1
                    # print(travel_time)
                else:
                    continue
            print(travel_time)
            return travel_time
        else:
            return 'no origin set'