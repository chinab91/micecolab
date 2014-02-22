from app import app, db
import flask.ext.whooshalchemy as whooshalchemy

class Exhibitor_Profile(db.Model):
    __tablename__ = 'exhibitor_profile'
    
    __searchable__ = ['location']

    id_exhibitor_profile = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(100))
    companyname = db.Column(db.String(100))
    position = db.Column(db.String(100))
    location = db.Column(db.String(100))

    def __init__(self, fullname, companyname, position, location):
    	self.fullname = fullname
    	self.companyname = companyname
    	self.position = position
    	self.location = location
    

whooshalchemy.whoosh_index(app, Exhibitor_Profile)

