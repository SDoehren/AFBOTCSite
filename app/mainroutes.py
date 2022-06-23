from flask import render_template,request,redirect,url_for,jsonify,make_response
from app import app


@app.route('/')
@app.route('/index')
def index():
    return "CAT"