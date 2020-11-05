from flask_login import UserMixin
from werkzeug.security import generate_password_hash

from .extensions import db 

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    password = db.Column(db.String(100))
    developer = db.Column(db.Boolean)
    lead = db.Column(db.Boolean)

    post = db.relationship(
        'Post', 
        foreign_keys='Post.posted_by_id', 
        backref='poster', 
        lazy=True
    )

    comment = db.relationship(
        'Post',
        foreign_keys='Post.commenter_id',
        backref='commenter',
        lazy=True
    )

    @property
    def unhashed_password(self):
        raise AttributeError('Cannot view unhashed password!')

    @unhashed_password.setter
    def unhashed_password(self, unhashed_password):
        self.password = generate_password_hash(unhashed_password)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    post = db.Column(db.Text)
    posted_by_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    commenter_id = db.Column(db.Text, db.ForeignKey('user.id'))