from app import db

class Exhibitor_Profile(db.Model):
    __tablename__ = 'exhibitor_profile'
    id_exhibitor_profile = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(100))
    companyname = db.Column(db.String(100))
    position = db.Column(db.String(100))
    location = db.Column(db.String(100))