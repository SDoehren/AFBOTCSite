from flask import render_template,request,redirect,url_for,jsonify,make_response
from app import app
from app import data

@app.route('/')
@app.route('/index')
def index():
    goodvsevil = [data.games[g] for g in data.games]
    goodvsevil = [[f"{g['session']}-{g['game']}",g['result']] for g in goodvsevil]
    goodvsevilscore = [len([x for x in goodvsevil if x[1]=="Good"]),
                       len([x for x in goodvsevil if x[1]=="Evil"])]


    return render_template('index.html', title="AFBOTC", goodvsevil = goodvsevil,goodvsevilscore=goodvsevilscore)

@app.route('/table/players/')
def table():
    return render_template('table.html', title="AFBOTC - Performance Table")

@app.route('/table/players/data/')
def playerdata():
    return data.games
