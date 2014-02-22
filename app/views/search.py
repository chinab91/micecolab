from flask import jsonify, Blueprint, render_template
from app import db
import datetime, time
from app.models import Exhibitor_Profile

mod = Blueprint('search', __name__)

@mod.route('/<search_id>', methods=['GET'])
def index(search_id):
	return '1'
    