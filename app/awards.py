from flask import render_template,request,redirect,url_for,jsonify,make_response
from app import app
from app import data
from random import sample

@app.route('/awards/')
def awardslist():
    awards = [data.awards[x] for x in data.awards]
    awards.sort(key=lambda x:x['name'])
    return render_template('awards.html', title="AFBOTC - Awards", awards = awards)
