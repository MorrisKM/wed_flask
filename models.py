from flask_restx import Resource, Namespace
from exts import db

class Course(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String, nullable= False, unique=True)
  description = db.Column(db.Text)
  credits = db.Column(db.Integer, default = 3)

  def save(self):
    db.session.add(self)
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()

  def update(self, name, description, credits):
    self.name = name
    self.description = description
    self.credits = credits

    db.session.commit()

