from dojo_ninjas.config.mysqlconnection import connectToMySQL
from dojo_ninjas.models import dojo_model

class Ninja:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo = None

    @classmethod
    def show_ninjas(cls,data):
        query = "select * from ninjas left join dojos on ninjas.dojo_id = dojos.id where dojos.id = %(id)s "
        results = connectToMySQL('ninja_dojo').query_db(query,data)
        # Create an empty list to append our instances of friends
        ninjas = []
        # Iterate over the db results and create instances of friends with cls.
        for ninja in results:
            ninjas.append( cls(ninja) )
        return ninjas
    
    @classmethod
    def save( cls , data ):
        query = "INSERT INTO ninjas ( first_name, last_name, age, dojo_id ) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s);"
        return connectToMySQL('ninja_dojo').query_db(query,data)

    @classmethod
    def edit_ninja(cls, data):
        query = "UPDATE ninjas SET first_name = %(first_name)s, last_name = %(last_name)s, age = %(age)s,updated_at=NOW() WHERE ninjas.id = %(id)s";
        
        return connectToMySQL('ninja_dojo').query_db(query,data)

    @classmethod
    def delete_ninja(cls, data):
        query = "DELETE FROM ninjas WHERE id = %(id)s";
        return connectToMySQL('ninja_dojo').query_db(query,data)   
    
    @classmethod
    def get_one_ninja(cls,data):
        query = "SELECT * FROM ninjas WHERE ninjas.id = %(id)s;"
        # query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojo_id = dojos.id WHERE dojos.id = %(id)s;"
        results = connectToMySQL('ninja_dojo').query_db(query,{'id': data})
        print(results)
        ninja = cls( results[0] )
        print("****")
        ninja.dojo = results[0]["dojo_id"]
        # for dojo in results:
        
        return ninja