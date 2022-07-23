from flask import flash
from flask_app import app
from flask_app.config.mysqlconnection import MySQLConnection, connectToMySQL
import re	
from flask_bcrypt import Bcrypt 
bcrypt = Bcrypt(app) 

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data ['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @staticmethod
    def validate_user(user):
        is_valid = True
        if len(user['first_name']) < 3:
            flash("First name must be 3 or more characters.")
            is_valid = False
        if len(user['first_name']) > 50:
            flash("First name must be less than 50 characters.")
            is_valid = False
        if len(user['last_name']) < 3:
            flash("Last name must be 3 or more characters.")
            is_valid = False
        if len(user['last_name']) > 50:
            flash("Last name must be less than 50 characters.")
            is_valid = False
        if not EMAIL_REGEX.match(user['email']): 
            flash("Invalid email address!")
            is_valid = False
        if len(User.get_by_email(user)) != 0:
            is_valid = False
            flash('Account already associated with given email')
        if len(user['password']) < 7:
            flash('*Password must be 8 or more characters*')
            is_valid = False
        if user['password'] != user['confirm_password']:
            is_valid = False
            flash('*Passwords must match*')
        return is_valid


    @classmethod
    def save(cls,data):
        query = "INSERT INTO user (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        result = connectToMySQL("user_login").query_db(query, data)

        return result

    @classmethod
    def get_by_email(cls,data):
        query = 'SELECT * FROM user WHERE email = %(email)s;'
        results = connectToMySQL('recipes_schema').query_db(query, data)
        
        if len(results[0]) < 1:
            return
        else:
            return cls(results[0])