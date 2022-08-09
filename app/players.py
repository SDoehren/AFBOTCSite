from flask import render_template,request,redirect,url_for,jsonify,make_response
from app import app
from app import data
from random import sample


@app.route('/players/')
def table():
    return render_template('playertable.html', title="AFBOTC - Performance Table")

@app.route('/api/players/')
def playerdata():
    return data.playertable
