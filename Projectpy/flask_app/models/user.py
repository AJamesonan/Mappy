from flask_app.config.mysqlconnection import MySQLConnection, connectToMySQL
import requests
import os

from flask import flash
from flask_app import app

from flask_bcrypt import Bcrypt 
bcrypt = Bcrypt(app) 
import re	
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

db='map_dashboard'

class User:
    def __init__(self, data):
        self.id = data['id']
        self.user_name = data['user_name']
        self.email = data['email']
        self.password = data ['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @staticmethod
    def validate_user(user):
        is_valid = True
        if len(user['user_name']) < 1:
            flash("name must be 2 or more characters.")
            is_valid = False
        if len(user['user_name']) > 50:
            flash("name must be less than 50 characters.")
            is_valid = False
        if not EMAIL_REGEX.match(user['email']): 
            flash("Invalid email address!")
            is_valid = False
        # if len(user.get_by_email(user)) != 0:
        #     is_valid = False
        #     flash('Account already associated with given email')
        if len(user['password']) < 7:
            flash('*Password must be 8 or more characters*')
            is_valid = False
        if user['password'] != user['confirm_password']:
            is_valid = False
            flash('*Passwords must match*')
        return is_valid


    @classmethod
    def save(cls,data):
        query = "INSERT INTO users (user_name, email, password) VALUES (%(user_name)s, %(email)s, %(password)s);"
        result = connectToMySQL(db).query_db(query, data)

        return result

    @classmethod
    def get_by_email(cls,data):
        query = 'SELECT * FROM users WHERE email = %(email)s;'
        results = connectToMySQL(db).query_db(query, data)
        
        if len(results) < 1:
            return False
        else:
            return cls(results[0])

    @classmethod
    def get_all_users():
        query = 'SELECT * FROM users;'
        results = connectToMySQL(db).query_db(query)
        users = []
        for user in results: 
            users.append(user)
        return results

    @classmethod
    def get_user_by_id(cls,data):  #use in create 
        query = 'SELECT * FROM users WHERE id = %(id)s;'
        results = connectToMySQL(db).query_db(query, data)
        return cls(results[0])