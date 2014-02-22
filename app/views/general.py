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


@mod.route('/discover')
def discover_recommendation():
	json_data = {
  "date": [
      
        {
          "name": "Errol Lim",
          "position": "CMO",
          "company": "Jublia",
          "location": "Table 2"
        },
        {
          "name": "Andriano",
          "position": "Lead Dev",
          "company": "eBay",
          "location": "E34"
        },
        {
          "name": "Andriano",
          "position": "Lead Dev",
          "company": "eBay",
          "location": "E34"
        },
        {
          "name": "Andriano",
          "position": "Lead Dev",
          "company": "eBay",
          "location": "E34"
        },
        {
          "name": "Andriano",
          "position": "Lead Dev",
          "company": "eBay",
          "location": "E34"
        }
  ]
}
	return jsonify(json_data)