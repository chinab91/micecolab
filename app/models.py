from app import db, login_serializer
from sqlalchemy.dialects.mysql import MEDIUMINT, SMALLINT, TIMESTAMP, TINYINT, TEXT
from flask.ext.security import UserMixin  # dependecies required : Flask-Security
from werkzeug.security import check_password_hash  # password hashing function, no dependencies required
#TODO: put default values, load from sql schema
#TODO: support tinyint, small text, etc. data types
from flask import json, jsonify
""" for natural language processing """
import nltk
""" re for regular expression """
import re
""" for sets in python """
from sets import Set
""" operator for sorting dictionary by value """
import operator
