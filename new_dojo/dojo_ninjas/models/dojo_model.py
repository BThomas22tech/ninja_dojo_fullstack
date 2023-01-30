# import the function that will return an instance of a connection
from dojo_ninjas.config.mysqlconnection import connectToMySQL
from dojo_ninjas.models.ninjas_model import Ninja

# model the class after the friend table from our database
class Dojo:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []
    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('ninja_dojo').query_db(query)
        # Create an empty list to append our instances of friends
        dojos = []
        # Iterate over the db results and create instances of friends with cls.
        for dojo in results:
            dojos.append( cls(dojo) )
        return dojos

    @classmethod
    def get_one_dojo(cls,data):
        query = "SELECT * from dojos where id = %(id)s"
        results = connectToMySQL('ninja_dojo').query_db(query,data)

        ninjas = []

        for ninja in results:
            ninjas.append(cls(ninja))
            return ninjas



    @classmethod
    def save_dojo(cls, data ):
        query = "INSERT INTO dojos (name, created_at, updated_at) VALUES ( %(name)s, now(), now() );"
        return connectToMySQL('ninja_dojo').query_db(query,data)

    @classmethod
    def get_dojo_with_ninjas( cls , data ):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(id)s;"
        results = connectToMySQL('ninja_dojo').query_db( query , data )
        # results will be a list of topping objects with the burger attached to each row. 
        
        dojo = cls( results[0] )
        for ninja in results:
            # Now we parse the burger data to make instances of burgers and add them into our list.
            ninja_data = {
                "id" : ninja["ninjas.id"],
                "first_name" : ninja["first_name"],
                "last_name" : ninja["last_name"],
                "age" : ninja["age"],
                "created_at" : ninja["ninjas.created_at"],
                "updated_at" : ninja["ninjas.updated_at"]
            }
            dojo.ninjas.append( Ninja( ninja_data ) )
        return dojo











    # @classmethod
    # def show_user(cls, data):
    #     query = "SELECT * FROM users WHERE id = %(id)s";
    #     results = connectToMySQL('user_cr').query_db(query,data)
    #     return  cls(results[0])
    
    # @classmethod
    # def edit_user(cls, data):
    #     query = "UPDATE users SET first_name=%(first_name)s,last_name=%(last_name)s,email=%(email)s,updated_at=NOW() WHERE id = %(id)s";
    #     return connectToMySQL('user_cr').query_db(query,data)
    # @classmethod
    # def delete_user(cls, data):
    #     query = "DELETE FROM users WHERE id = %(id)s";
    #     return connectToMySQL('user_cr').query_db(query,data)
        

