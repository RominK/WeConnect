from flask import Flask 
from flask_restful import Api, Resource, abort

from models import User, Business, Review

from resources.reviews import reviews_api
from resources.businesses import businesses_api

app = Flask(__name__)

app.register_blueprint(businesses_api, url_prefix='/api/v1')
app.register_blueprint(reviews_api, url_prefix='/api/v1')


if __name__ == '__main__':
    app.run(debug = True)