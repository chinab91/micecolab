from flask import jsonify, Blueprint, render_template
from app import db
#from app.models import (Attendee_Login, Attendee_Profile, Attendee_Match, Event_Info, Timestamp_Lookout

mod = Blueprint('general', __name__)

@mod.route('/')
def index():
    return render_template('index.html')

@mod.route('/get_meetings')
def get_meetings():
	return 'get meetings';