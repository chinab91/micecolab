from flask import jsonify, Blueprint, render_template, url_for, redirect, session
from app import db
import datetime, time
import arrow
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
def index():
    try:
        session["access"]
        return render_template('index.html')
    except:
        return render_template('index.html')

@mod.route('/get_meetings')
def get_meetings():
    json_date = {
  "date": [
    {
      "value": "22 Feb 2014",
      "meetings": [
        {
          "cell_status": get_cell_status(2014, 02, 22, 14, 00, 00),
          "time": "2:00 PM",
          "name": "Stefano Lenzini",
          "position": "Lead Engineer",
          "company": "Ferrari",
          "location": "Booth B190"
        },
        {
          "cell_status": get_cell_status(2014, 02, 22, 14, 00, 00),
          "time": "3:00 PM",
          "name": "Elogio Berardinelli",
          "position": "Lead Mechanic",
          "company": "Maserati",
          "location": "Booth C110"
        }
      ]
    },
    {
      "value": "23 Feb 2014",
      "meetings": [
        {
          "cell_status": get_cell_status(2014, 02, 23, 14, 00, 00),
          "time": "10:00 AM",
          "name": "Kamioka Hiroya",
          "position": "Purchasing Manager",
          "company": "Honda Motor",
          "location": "Booth B523"
        },
        {
          "cell_status": get_cell_status(2014, 02, 23, 16, 00, 00),
          "time": "04:00 PM",
          "name": "Harald Ecker",
          "position": "Assistant Manager",
          "company": "Mercedes Benz",
          "location": "Booth A121"
        },
        {
          "cell_status": get_cell_status(2014, 02, 23, 17, 00, 00),
          "time": "05:00 PM",
          "name": "Rene Wosnitza",
          "position": "Lead Engineer",
          "company": "BMW",
          "location": "Booth D128"
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
  "discover": [
      
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


@mod.route('/activity')
def activity():
  json_data = {
 "activity": [
   {
     "time": "%s " % arrow.now().replace(minutes=15).format('HH:mm')
   },
   {
     "time": "%s " % arrow.now().replace(minutes=30).format('HH:mm')
   },
   {
     "time": "%s " % arrow.now().replace(minutes=30).format('HH:mm')
   }
 ]
}
  return jsonify(json_data)


@mod.route('/bot')
def bot():
    return render_template('chat.html')


@mod.route('/api', methods=['GET'])
def api():
    if request.environ.get('wsgi.websocket'):
        ws = request.environ['wsgi.websocket']
        #ws.send("Welcome to the app. How can I help you")
        while True:
            message = ws.receive()
            if message == 'a':
              ws.send("cats")
            else:
              ws.send("dogs")
    return

