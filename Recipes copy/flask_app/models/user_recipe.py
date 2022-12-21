
from flask import flash
from flask_app import app
from flask_app.models.user import User
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

    @staticmethod
    def recipe_is_valid(recipe):
        is_valid = True
        if recipe['name'] == "":
            flash('Name must not be empty')
            is_valid = False
        if recipe['description'] == "":
            flash('Description must not be empty')
            is_valid = False
        if recipe['instructions'] == "":
            flash('instructions must not be empty')
            is_valid = False
        if recipe['date_cooked'] == "":
            flash('date cooked must not be empty')
            is_valid = False
        if len(recipe['name']) < 3:
            flash('Name must be more than 3 characters')
            is_valid = False
        if len(recipe['description']) < 3:
            flash('descrption must be more than 3 characters')
            is_valid = False
        if len(recipe['instructions']) < 3:
            flash('Instructions must be more than 3 characters')
            is_valid = False
        return is_valid

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

    @classmethod
    def get_recipes_and_users(cls):
        query = 'SELECT * FROM recipes JOIN users ON recipes.user_id = users.id;'
        results =  connectToMySQL('recipes_schema').query_db(query)
        list_recipes = []
        for row in results:
            current_recipe = cls(row)
            user_data = {
                **row,  ##grabs all user info from the row --> list
                "created_at": row['users.created_at'],
                'updated_at': row['users.updated_at'],
                'id': row['users.id']
            }
            current_user = User(user_data)
            current_recipe.user = current_user
            list_recipes.append(current_recipe)
        return list_recipes

    @classmethod
    def update_one(cls,data):
        query = 'UPDATE recipes SET name = %(name)s, description = %(description)s,instructions = %(instructions)s, date_cooked = %(date_cooked)s, under_30 = %(under_30)s, user_id = %(user_id)s WHERE id = %(id)s;'
        return connectToMySQL('recipes_schema').query_db(query,data)

    classmethod
    def delete_one(data):
        query = 'DELETE FROM recipes WHERE id = %(id)s;'
        return connectToMySQL('recipes_schema').query_db(query,data)


