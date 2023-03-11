from flask_app.config.mysqlconnection import connectToMySQL

class Ninjas:
    DB = "dojos_and_ninjas_schema"
    def __init__(self, data):
        self.id = data['id']
        self.dojo_id = data['dojo_id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save_ninja(cls, data):
        query = """INSERT into ninjas (dojo_id,first_name, last_name, age)
        VALUES (%(dojo_id)s, %(first_name)s, %(last_name)s, %(age)s); 
        """ 
        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def get_all_ninjas(cls):
        query = """
        SELECT * FROM ninjas;
        """
        results = connectToMySQL(cls.DB).query_db(query)
        ninjas = []
        for ninja in results:
            ninjas.append(cls(ninja))
        return ninjas
    
    @classmethod
    def get_one_ninja(cls, data):
        query = """
        SELECT * FROM ninjas WHERE ninjas.id = %(id)s;
        """
        results = connectToMySQL(cls.DB).query_db(query, data)
        return cls(results[0])
    
    @classmethod
    def update_ninja(cls, data):
        query="""
        UPDATE ninjas SET first_name = %(first_name)s, last_name = %(last_name)s, age = %(age)s WHERE id = %(id)s
        """
        return connectToMySQL(cls.DB).query_db(query,data)
    
    
    @classmethod
    def delete_ninja(cls, data):
        query= """
        DELETE FROM ninjas WHERE id = %(id)s;
        """
        return connectToMySQL(cls.DB).query_db(query, data)