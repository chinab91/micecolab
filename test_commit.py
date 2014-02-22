from app import db
from app.models import Exhibitor_Profile

exhibitor = Exhibitor_Profile(fullname='a', location='b', position='c', companyname='test')
db.session.add(exhibitor)
db.session.commit()