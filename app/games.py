from flask import render_template,request,redirect,url_for,jsonify,make_response
from app import app
from app import data


@app.route('/games/')
@app.route('/games/<gameid>')
def games(gameid = None):
    games = data.games
    if gameid is None:
        gameid = list(games.keys())[-1]
    game = games[gameid]

    #print(game['playerdata'])

    allkeys = list(games.keys())*2
    gameindex = allkeys.index(gameid)

    sessions = []
    sessionsaptures = []
    for gid in list(games.keys()):
        if games[gid]['session'] not in sessionsaptures:
            sessionsaptures.append(games[gid]['session'])
            pack = [gid,f"Session {games[gid]['session']} - {games[gid]['date']}"]
            sessions.append(pack)

    print(game.keys())
    STs = " | ".join(games[gid]['storytellers'])
    return render_template('games.html', title=f"AFBOTC - {gameid}",
                           gamelist = sessions, last=allkeys[gameindex-1], next=allkeys[gameindex+1], gamedetails=game,
                           STs=STs)