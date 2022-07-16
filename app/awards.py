from flask import render_template,request,redirect,url_for,jsonify,make_response
from app import app
from app import data
from random import sample

@app.route('/awards/')
def awardslist():
    awards = [data.awards[x] for x in data.awards]
    order = {'winningestplayer': 1, 'winningestrole': 2, 'stickyfingers': 3, 'goodest': 4, 'switchhitter': 5,
             'fingerpointer': 6, 'demonhunter': 7, 'pickme': 8, 'earlygoose': 9, 'themint': 10, 'novote': 11,
             'whome': 12}

    awards.sort(key=lambda x:order.get(x['name'], 999))

    return render_template('awards.html', title="AFBOTC - Awards", awards = awards)
