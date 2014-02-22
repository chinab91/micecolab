from flask import jsonify, Blueprint, render_template
from app import db
import datetime, time, pprint
from app.models import Exhibitor_Profile

mod = Blueprint('search', __name__)

@mod.route('/<search_id>', methods=['GET'])
def index(search_id):
	search_results = db.session.query(Exhibitor_Profile).filter((Exhibitor_Profile.location.like('%%%s%%' % search_id)) | (Exhibitor_Profile.fullname.like('%%%s%%' % search_id)) | (Exhibitor_Profile.companyname.like('%%%s%%' %  search_id)) | (Exhibitor_Profile.position.like('%%%s%%' %  search_id))).all()
	#pprint.pprint(search_results)
	
	search = []
	for search_result in search_results:
		search_element = {}
		search_element['fullname'] = search_result.fullname
		search_element['position'] = search_result.position
		search_element['companyname'] = search_result.companyname
		search_element['location'] = search_result.location
		search.append(search_element)

	return jsonify({"search": search})


