from flask_restful import Resource
from flask import redirect

from models.url import URLModel


class URL(Resource):

    def get(self, short_url):
        url = URLModel.find_by_short_url(short_url)
        if url is None:
            return {"message": "Page not found."}, 404
        url.hits = url.hits + 1
        try:
            url.save_to_db()
        except Exception as e:
            return {"message": "An error occured updating the url."}, 500
        return redirect(url.main_url, code=302)
