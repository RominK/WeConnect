from flask import Model

class User():
    def __init__(self, username, firstname, lastname, email):
        username = self.username
        firstname = self.firstname
        lastname = self.lastname
        email = self.email

class Business():
    def __init__(self, name, description, owner_id, category, location):
        name =  self.name
        owner = self.owner
        description = self.description
        category = self.category
        location = self.location

class Review():
    def __init__(self, business_id, reviewer_id, comment, rating):
        reviewer_id = self.reviewer_id
        comment = self.comment
        rating = self.rating




