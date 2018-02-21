from flask import Flask, jsonify

from flask_restful import Resource, abort, Api

from models import User


Users = {
    1: User('user1', 'rom1', 'kay1', 'user1@wecon.com'),
    2: User('user2', 'rom2', 'kay2', 'user2@wecon.com'),
    3: User('user3', 'rom3', 'kay3', 'user3@wecon.com')

}


class User(Resource):
    """
    register user
    get one user
    """

    def get(self):
        return 0