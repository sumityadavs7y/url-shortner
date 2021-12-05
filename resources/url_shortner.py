from flask_restful import Resource, reqparse
import random
import string
import validators
import urllib3
from bs4 import BeautifulSoup

from models.url import URLModel

http = urllib3.PoolManager()


class URLShortner(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('url',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )

    def post(self):
        data = URLShortner.parser.parse_args()

        main_url = data['url']
        if not validators.url(main_url):
            return {"message": "Not a valid URL."}, 400

        response = http.request('GET', main_url)
        soup = BeautifulSoup(response.data, features="html.parser")
        title = soup.title.string
        short_url = ''.join(random.choice(string.ascii_letters)
                            for i in range(6))
        url = URLModel(main_url, short_url, title)
        try:
            url.save_to_db()
        except Exception as e:
            return {"message": "An error occured inserting the url."}, 500
        return url.json(), 201
