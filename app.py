from flask import Flask
from flask_restful import Resource, Api

from db import db
from resources.home import Home
from resources.url_shortner import URLShortner
from resources.url import URL

app = Flask(__name__)
# configs will be placed here
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()


api.add_resource(Home,'/')
api.add_resource(URLShortner, '/url')
api.add_resource(URL, '/<short_url>')

if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)