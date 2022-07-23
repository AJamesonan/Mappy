from flask_app.config.mysqlconnection import MySQLConnection, connectToMySQL
# from flask_app.controllers.users import delete_user

class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email= data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM users;'
        results = connectToMySQL('users_schema').query_db(query)
        users = []
        for user in results:
            users.append(cls(user))
        return users


    @classmethod
    def create_user(cls,data):
        query = 'INSERT INTO users (first_name, last_name,email,created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, NOW(), NOW());'
        return connectToMySQL('users_schema').query_db(query,data)
    

    @classmethod
    def get_user_by_id(cls,data):

        query = 'SELECT * FROM users WHERE id = %(id)s;'
        
        results = connectToMySQL('users_schema').query_db(query,data)

        user = User(results[0])
        return user


    @classmethod
    def update_user(cls,data):
        query = 'UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s WHERE id = %(id)s;'
        MySQLConnection ("users_schema").query_db(query,data)


    @classmethod
    def delete_user(cls,data):
        query = 'DELETE FROM users WHERE id = %(id)s;'
        MySQLConnection ("users_schema").query_db(query,data)

    @classmethod
    def get_user(cls, data):
        query = 'SELECT first_name, last_name, email, created_at, updated_at FROM users WHERE id = %(id)s;'
        return connectToMySQL('users_schema').query_db(query,data)