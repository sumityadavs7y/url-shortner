from datetime import datetime
from flask import request

from db import db


class URLModel(db.Model):
    __tablename__ = 'urls'

    id = db.Column(db.Integer, primary_key=True)
    main_url = db.Column(db.String(256), nullable=False)
    short_url = db.Column(db.String(80), unique=True, nullable=False)
    title = db.Column(db.String(256))
    hits = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.now())

    def __init__(self, main_url, short_url, title):
        self.main_url = main_url
        self.short_url = short_url
        self.title = title

    def json(self):
        current_time = datetime.now()
        time_diff = current_time - self.created_at
        duration_in_s = time_diff.total_seconds()
        days = divmod(duration_in_s, 86400)
        hours = divmod(days[1], 3600)[0]
        if hours == 0:
            hours = 1
        hourly_hits = self.hits/hours
        return {
            'id': self.id,
            'main_url': self.main_url,
            'short_url': request.root_url + self.short_url,
            'hits': self.hits,
            'hourly_hits': hourly_hits,
            'title': self.title
        }

    @classmethod
    def find_by_title(cls, keyword):
        return cls.query.filter(cls.title.like(f'%{keyword}%'))

    @classmethod
    def find_by_short_url(cls, short_url):
        return cls.query.filter_by(short_url=short_url).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
