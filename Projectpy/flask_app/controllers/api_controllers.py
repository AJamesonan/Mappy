from flask import render_template,redirect,request,session,flash
from flask_app import app
import re	
from flask_app.models.user import User
from flask_app.models.place import Place
import requests
import os

@app.route('/places/placeid')
def get_placeid(place):
        api_request = requests.get("https://www.google.com/maps/api/geocode/json?address=" + place.street_address+ " "+ place.city + " "+ place.state + " "+ place.zip +"&key="+ os.environ.get("FLASK_APP_API_KEY"))
        print(api_request)
