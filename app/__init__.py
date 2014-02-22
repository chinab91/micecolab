from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask.ext.mail import Mail  # module to send email, used to support password recovery


from config import SQLALCHEMY_DATABASE_URI


app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

from views import general

app.register_blueprint(general.mod, url_prefix='/general')