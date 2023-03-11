from flask_app.config.mysqlconnection import connectToMySQL
from .ninja import Ninjas

class Dojos:
    DB = "dojos_and_ninjas_schema"
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def get_all_dojos(cls):
        query =  """
        SELECT * FROM dojos;
        """
        results = connectToMySQL(cls.DB).query_db(query)
        print(results)

        dojos = []
        for x in results:
            dojos.append(cls(x))
        return dojos
    
    @classmethod
    def save_dojo(cls, data):
            query = """INSERT into dojos (name, created_at, updated_at)
            VALUES (%(name)s, NOW(), NOW()); 
            """ 
            results = connectToMySQL(cls.DB).query_db(query, data)
            return results
    
    @classmethod
    def get_one_dojo(cls, data):
        query = """
        SELECT * FROM dojos WHERE id = %(id)s;
        """
        results = connectToMySQL(cls.DB).query_db(query, data)
        return cls(results[0])
    
    @classmethod
    def update_dojo(cls, data):
        query="""
        UPDATE dojos SET name = %(name)s WHERE id = %(id)s
        """
        return connectToMySQL(cls.DB).query_db(query,data)
    
    
    @classmethod
    def delete_dojo(cls, id):
        query= """
        DELETE FROM dojos WHERE id = %(id)s;
        """
        data = {"id": id}
        results = connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def dojo_with_ninjas(cls, data):
        query = """
            SELECT * FROM dojos
            LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id
            WHERE dojos.id = %(id)s;
            """
        results= connectToMySQL(cls.DB).query_db(query, data)
        one_dojo = cls(results[0])
        for row in results:
            ninja_data={
                "id": row["ninjas.id"],
                "dojo_id": row["dojo_id"],
                "first_name": row["first_name"],
                "last_name": row["last_name"],
                "age": row["age"],
                "created_at": row["created_at"],
                "updated_at": row["updated_at"]
            }
            one_dojo.ninjas.append(Ninjas(ninja_data))
        return one_dojo