from flask import jsonify, Blueprint, render_template, url_for, redirect, session
from app import db
import datetime, time
#from app.models import (Attendee_Login, Attendee_Profile, Attendee_Match, Event_Info, Timestamp_Lookout

mod = Blueprint('general', __name__)

@mod.route('/<passcode_string>')
def check_passcode(passcode_string):
    passcode_file = open('app/views/passcode.txt')
    passcode = passcode_file.readline()
    if False: #passcode_string != "":
        return "404"
    else:
        session["access"] = True
        return redirect(url_for('general.index')) # pending return template

@mod.route('/')
@mod.route('/index')
def index():
    if session["access"]:
        return render_template('index.html')
    else:
        return "Sorry no access"

@mod.route('/get_meetings')
def get_meetings():
    json_date = {
  "date": [
    {
      "value": "21 Feb 2014",
      "meetings": [
        {
          "cell_status": get_cell_status(2014, 02, 21, 14, 00, 00),
          "time": "2pm",
          "name": "Errol Lim",
          "position": "CMO",
          "company": "Jublia",
          "location": "Table 2"
        },
        {
          "cell_status": get_cell_status(2014, 02, 21, 15, 00, 00),
          "time": "3pm",
          "name": "Andriano",
          "position": "Lead Dev",
          "company": "eBay",
          "location": "E34"
        }
      ]
    },
    {
      "value": "22 Feb 2014",
      "meetings": [
        {
          "cell_status": get_cell_status(2014, 02, 22, 14, 00, 00),
          "time": "2pm",
          "name": "KY",
          "position": "CEO",
          "company": "Jublia",
          "location": "Table 8"
        },
        {
          "cell_status": get_cell_status(2014, 02, 22, 14, 00, 00),
          "time": "2pm",
          "name": "KY",
          "position": "CEO",
          "company": "Jublia",
          "location": "Table 8"
        },
        {
          "cell_status": get_cell_status(2014, 02, 22, 17, 16, 00),
          "time": "6pm",
          "name": "KY",
          "position": "CEO",
          "company": "Jublia",
          "location": "Table 8"
        }
      ]
    },
    {
      "value": "23 Feb 2014",
      "meetings": [
        {
          "cell_status": get_cell_status(2014, 02, 23, 14, 00, 00),
          "time": "2pm",
          "name": "KY",
          "position": "CEO",
          "company": "Jublia",
          "location": "Table 8"
        },
        {
          "cell_status": get_cell_status(2014, 02, 23, 15, 00, 00),
          "time": "3pm",
          "name": "KY",
          "position": "CEO",
          "company": "Jublia",
          "location": "Table 8"
        }
      ]
    }
  ]
}

    return jsonify(json_date)

def get_cell_status(year, month, date, hour, min, sec):
    dt = datetime.datetime(year, month, date, hour, min, sec)
    unixts = time.mktime(dt.timetuple())

    currentdt = datetime.datetime.now()
    currentunixts = time.mktime(currentdt.timetuple())

    if(unixts > currentunixts):
        return 1
    else:
        return 0



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