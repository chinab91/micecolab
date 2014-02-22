from flask import jsonify, Blueprint, render_template
from app import db
import datetime, time, pprint
from app.models import Exhibitor_Profile

mod = Blueprint('search', __name__)

@mod.route('/<search_id>', methods=['GET'])
def index(search_id):
	
	pprint.pprint(a)
	return '1'