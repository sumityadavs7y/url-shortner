from flask_restful import Resource

from models.url import URLModel


class Search(Resource):
    def get(self, keyword):
        urls = URLModel.find_by_title(keyword)
        return {"urls": [url.json() for url in urls]}, 200
