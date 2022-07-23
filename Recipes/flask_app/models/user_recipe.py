from flask import flash
from flask_app import app
from flask_app.config.mysqlconnection import MySQLConnection, connectToMySQL
import re	
from flask_bcrypt import Bcrypt 
bcrypt = Bcrypt(app) 
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class Recipe:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.under_30 = data['under_30']
        self.posted_by = data['posted_by']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date_cooked= data['date_cooked']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_recipes_by_user_id(cls, data):
        query = 'SELECT * FROM recipes WHERE user_id=%(user_id)s;'
        results = connectToMySQL('recipes_schema').query_db(query,data)
        recipes = []
        for recipe in results:
            recipes.append(cls(recipe))
        return recipes

    @classmethod
    def save_recipe(cls,data):
        query = "INSERT INTO recipes (name, under_30, posted_by, description, instructions, date_cooked, user_id) VALUES (%(name)s, %(under_30)s, %(posted_by)s, %(description)s, %(instructions)s, %(date_cooked)s, %(user_id)s);"
        connectToMySQL("recipes_schema").query_db(query, data)
        return

    @classmethod
    def get_recipe_by_id(cls,data):
        query = 'SELECT * FROM recipes WHERE id = %(id)s'

        results = connectToMySQL("recipes_schema").query_db(query, data)
        
        return cls(results[0])

