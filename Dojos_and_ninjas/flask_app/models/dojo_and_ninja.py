from flask_app.config.mysqlconnection import MySQLConnection, connectToMySQL

class Dojo:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def get_all_dojos(cls):
        query = 'SELECT * FROM dojos;'
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)

        dojos = []
        for dojo in results:
            dojos.append(cls(dojo))

        return dojos

    @classmethod
    def create_dojo(cls,data):
        query = 'INSERT INTO dojos (name) VALUES (%(name)s);'
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
    
    @classmethod 
    def get_dojo_by_id(cls,data):
        query = 'SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;'
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        dojo = Dojo(results[0])
        for row in results:
            if row['ninjas.id'] != None:
                ninja_data = {
                    'id': row['ninjas.id'],
                    'first_name': row['first_name'],
                    'last_name': row['last_name'],
                    'age': row['age'],
                    'created_at': row['ninjas.created_at'],
                    'updated_at': row['ninjas.updated_at'],
                    'dojo_id' : row['dojo_id'],
                }
                new_ninja = Ninja(ninja_data)
                dojo.ninjas.append(new_ninja)
        return dojo


class Ninja:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']


    @classmethod
    def create_ninja(cls,data):
        query = 'INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s);'
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
