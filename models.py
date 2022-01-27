from app import db
from sqlalchemy import exc

import errors

class BaseModelMixin:

    @classmethod
    def by_id(cls, obj_id):
        obj = cls.query.get(obj_id)
        if obj:
            return obj
        else:
            raise errors.NotFound

    def add(self):
        db.session.add(self)
        try:
            db.session.commit()
        except exc.IntegrityError:
            raise errors.BadLuck

    def delete(cls, obj_id):
        obj = cls.query.get(obj_id)
        db.session.delete(obj)
        try:
            db.session.commit()
        except exc.IntegrityError:
            raise errors.BadLuck

class Advertisement(db.Model, BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=True)
    description = db.Column(db.String(250))
    date_of_creation = db.Column(db.DateTime)
    owner = db.Column(db.String(40))

    def __str__(self):
        return '<Advertisement {}>'.format(self.title)

    def __repr__(self):
        return str(self)

    def to_dict(self):
        return {
            'title': self.title,
            'description': self.description,
            'date_of_creation': self.date_of_creation,
            'owner': self.owner
        }