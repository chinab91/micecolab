from flask import jsonify, Blueprint
mod = Blueprint('general', __name__)

@mod.route('/passcode_check/<passcode_string>')
def check_passcode(passcode_string):
	passcode_file = open('app/views/passcode.txt')
	passcode = passcode_file.readline()
	if passcode_string != passcode:
		return "wrong passcode" # pending retrun template
	else:
		return "right passcode" # pending return template