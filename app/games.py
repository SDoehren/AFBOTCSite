from flask import render_template,request,redirect,url_for,jsonify,make_response
import json
from app import app
from app import data


@app.route('/games/')
def gamestable():
    players = []
    roles = []
    dates = []
    sessions = []
    scripts = []
    results = []
    winmethods = []
    playercounts = []
    storytellers = []

    for g in data.gamessummary:
        players += data.gamessummary[g]['playerorder']
        roles += data.gamessummary[g]['allrolesused']
        dates += [data.gamessummary[g]['date']]
        sessions += [data.gamessummary[g]['session']]
        scripts += [data.gamessummary[g]['script']]
        results += [data.gamessummary[g]['result']]
        winmethods += [data.gamessummary[g]['winmethod']]
        playercounts += [data.gamessummary[g]['players']]
        storytellers += data.gamessummary[g]['storytellers']

    players = list(set(players))
    players.sort()

    roles = list(set(roles))
    roles.sort()

    dates = list(set(dates))
    dates.sort()

    sessions = list(set(sessions))
    sessions.sort()

    scripts = list(set(scripts))
    scripts.sort()

    results = list(set(results))
    results.sort()

    winmethods = list(set(winmethods))
    winmethods.sort()

    playercounts = list(set(playercounts))
    playercounts.sort()

    storytellers = list(set(storytellers))
    storytellers.sort()

    return render_template('gamestable.html', title="AFBOTC - Games",
                           players=players, roles=roles, dates=dates, sessions=sessions, scripts=scripts,
                           results=results, winmethods=winmethods, playercounts=playercounts, storytellers=storytellers)

@app.route('/api/gamestable/')
def tableapi():
    return data.gamessummary


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
    STS = " | ".join(game['storytellers'])
    return render_template('games.html', title=f"AFBOTC - {gameid}",
                           gamelist = sessions, last=allkeys[gameindex-1], next=allkeys[gameindex+1], gamedetails=game,
                           STS=STS)