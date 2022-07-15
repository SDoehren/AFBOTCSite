from flask import render_template,request,redirect,url_for,jsonify,make_response
from app import app
from app import data
from random import sample

@app.route('/')
@app.route('/index')
def index():
    goodvsevil = [data.games[g] for g in data.games]
    goodvsevil = [[f"{g['session']}-{g['game']}",g['result']] for g in goodvsevil]
    goodvsevilscore = [len([x for x in goodvsevil if x[1] == "Good"]),
                       len([x for x in goodvsevil if x[1] == "Evil"])]

    goodvsevilper = round((goodvsevilscore[0]/(goodvsevilscore[0]+goodvsevilscore[1]))*100)

    goodvsevillast15 = goodvsevil[-15:]
    goodvsevillast15score = [len([x for x in goodvsevillast15 if x[1] == "Good"]),
                       len([x for x in goodvsevillast15 if x[1] == "Evil"])]
    goodvsevillast15per = round((goodvsevillast15score[0] / (goodvsevillast15score[0] + goodvsevillast15score[1])) * 100)

    awardsum = [{"title":x,"name":data.awards[x]["name"],"winners":data.awards[x]['winners'],
                 "note":data.awards[x]['details'],
                 "score":data.awards[x]['score']} for x in data.awards]

    awardsum = sample(awardsum,min([12,len(awardsum)]))

    return render_template('index.html', title="AFBOTC", goodvsevil = goodvsevil,goodvsevilscore=goodvsevilscore,
                           goodvsevilper=goodvsevilper, goodvsevilscorelast15=goodvsevillast15score,
                           goodvsevillast15per=goodvsevillast15per,awards = awardsum)

@app.route('/players/')
def table():
    return render_template('table.html', title="AFBOTC - Performance Table")

@app.route('/players/data/')
def playerdata():
    return data.games
