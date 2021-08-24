from flask_login import UserMixin
from sqlalchemy.sql import func

from website.extensions import db

class User(db.Model, UserMixin):
  """A basic representation of a user."""
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(150), unique=True)
  password = db.Column(db.String(25), nullable=False)
  first_name = db.Column(db.String(150), nullable=False)
  notes = db.relationship('Note')

  def __repr__(self):
    return f'User: <{self.email}, {self.first_name}>'

class Note(db.Model):
  """A basic representation of a note."""
  id = db.Column(db.Integer, primary_key=True)
  date_posted = db.Column(db.DateTime(timezone=True), default=func.now())
  title = db.Column(db.String(200))
  text = db.Column(db.String(1000))
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

  def __repr__(self):
    return f'Post: <{self.title}, {self.text}>'
