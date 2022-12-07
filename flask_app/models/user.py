from flask_app.config.mysqlconnection import connectToMySQL
import re
from flask import flash

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create(cls,data):
        # query = "INSERT INTO users (first_name,last_name,email,password,created_at,updated_at) VALUES (%(first_name)s,%(last_name)s,%(email)s,%(password)s,%(created_at)s,%(updated_at)s)"
        # return connectToMySQL("buystuff_db").query_db(query,data)

        query = "INSERT INTO users (first_name,last_name,email,password) VALUES (%(first_name)s,%(last_name)s,%(email)s,%(password)s)"
        return connectToMySQL("buystuff_db").query_db(query,data)

    @classmethod
    def find_by_email(cls,data):
        query = "SELECT * from users WHERE email = %(email)s"
        results = connectToMySQL("buystuff_db").query_db(query,data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @staticmethod
    def validate(data):
        is_valid = True
        data_for_email_validator = {
            'email': data['email']
        }

        if len(data['first_name']) < 2:
            is_valid = False
            flash("First name must be at least 2 characters long.")
        if len(data['last_name']) < 2:
            is_valid = False
            flash("Last name must be at least 2 characters long.")
        if not EMAIL_REGEX.match(data['email']): 
            is_valid = False
            flash("Invalid email address!")
        if User.find_by_email(data_for_email_validator):
            is_valid = False
            flash("Email already in use.")
        return is_valid