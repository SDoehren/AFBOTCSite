from flask import Flask,url_for
import os
from flask_cors import CORS

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or 'FD29E48FB911DD1A858D1FCF246E3'

from app import mainroutes
from app import data
from app import games
from app import awards

