from flask import Flask 
from flask_restful import Api, Resource, abort

from models import User, Business, Review

app = Flask(__name__)
api = Api(app)

#def __init__(self, username, firstname, lastname, email):
# def __init__(self, name, description, owner_id, category, location):


Users = {
    1: User('user1', 'rom1', 'kay1', 'user1@wecon.com')
    2: User('user2', 'rom2', 'kay2', 'user2@wecon.com')
    3: User('user3', 'rom3', 'kay3', 'user3@wecon.com')

}


Businesses = {
    1: Business('Buz1', 'short description', 1, 'cat1', 'loc1')
    2: Business('Buz2', 'short description2', 2, 'cat2', 'loc2')
    3: Business('Buz3', 'short description3', 3, 'cat3', 'loc3')

}
# def __init__(self, reviewer_id, comment, rating):

Reviews = {
1: Reviewer(1, 2, 'short comment', 5)
2: Reviewer(2, 3, 'short comment', 9)
1: Reviewer(3, 1, 'short comment', 7)
}


def abort_if_business_doesnt_exist(business_id):
    if business_id not in Businesses:
        abort(404, message="Business {} doesn't exist".format(business_id))

##User authentication still missing


class Business(Resource):
    """
    retrieve one business
    delet a business
    update a business
    """
    def get(self, business_id):
        abort_if_business_doesnt_exist(business_id)
        return Businesses[business_id]

    def delete(self, business_id):
        abort_if_business_doesnt_exist(business_id)
        del Businesses[business_id]
        return '', 204

    def put(self, business_id):
        args = parser.pasrse_args()
        business = Business(args)
        Businesses[business_id]=business
        return task, 201



class BusinessList(Resource):
    """
    List all businesses
    Add a business to the list of businesses
    """

    def get(self):
        return Businesses

    def post(self):
        args = parser.parse_args()
        business_id = int(max(Businesses.keys() + 1)
        Businesses[business_id]=Business(args)
        return Businesses[business_id], 201

    def Reviews(self):
        """
        List all reviews of a business
        Add a new review to the list of a business
        """
        def get(self, business_id):
            reviews = []
            for review in Reviews:
                if review.business_id == business_id:
                    reviews.add(review)
            return reviews 

        def post(self, business_id):
            args = parse.parse_args()
            review_id = int(max(Reviews.keys() + 1))
            Reviews[review_id] = Review(args)

## set up Api resource routing

api.add_resource(Business, 'api/businesses/<businessId>' )

api.add_resource(Businesses, '/api/businesses')

api.add_resource(Reviews, '/api/businesses/<businessId>/reviews')


if __name__ == '__main__':
    app.run(debug = True)