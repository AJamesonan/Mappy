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
        # if len(User.get_by_email(user)) != 0:
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
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        result = connectToMySQL("recipes_schema").query_db(query, data)

        return result

    @classmethod
    def get_by_email(cls,data):
        query = 'SELECT * FROM users WHERE email = %(email)s;'
        results = connectToMySQL('recipes_schema').query_db(query, data)
        
        if len(results) < 1:
            return False
        else:
            return cls(results[0])

    @classmethod
    def get_all_users():
        query = 'SELECT * FROM users;'
        results = connectToMySQL('recipes_schema').query_db(query)
        users = []
        for user in results: #maybe useless??
            users.append(user)
        return results

    @classmethod
    def get_user_by_id(cls,data):  #use in create recipe
        query = 'SELECT * FROM users WHERE id = %(id)s;'
        results = connectToMySQL('recipes_schema').query_db(query, data)
        return cls(results[0])
        # query = 'SELECT * FROM users LEFT JOIN recipes ON users.id = recipes.user_id WHERE users.id = %(id)s;'
        # results = connectToMySQL('recipes_schema').query_db(query,data)
        # user = User(results[0])
        # for recipe in results:
        #     if recipe['recipes.id'] != None:
        #         recipe_data = {
        #             'id' : recipe['id'],
        #             'name' : recipe['name'],
        #             'under_30' : recipe['under_30'],
        #             'posted_by' : recipe['posted_by'],
        #             'description' : recipe['description'],
        #             'instructions' : recipe['instructions'],
        #             'date_cooked': recipe['date_cooked']
        #         }
        #         new_recipe = Recipes(recipe_data)
        #         user.recipes.append(new_recipe)
        # return user

