from flask import jsonify, Blueprint
mod = Blueprint('general', __name__)

@mod.route('/sms', methods=['GET'])
def get_sms_details():
	return '1'