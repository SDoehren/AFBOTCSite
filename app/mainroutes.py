from flask import render_template,request,redirect,url_for,jsonify,make_response
from app import app


@app.route('/')
@app.route('/index')
def index():
    goodvsevil = [['1-1','Good'],['1-2','Good'],['2-1','Good'],['2-2','Evil'],['2-3','Good'],['2-4','Good'],['3-1','Good'],['3-2','Good'],['4-1','Good'],['4-2','Good'],['4-3','Good'],['4-4','Good'],['4-5','Good'],['4-6','Good'],['4-7','Good'],['4-8','Good'],['5-1','Good'],['5-2','Evil'],['5-3','Good'],['6-1','Good'],['6-2','Evil'],['7-1','Good'],['7-2','Evil'],['7-3','Good'],['7-4','Good'],['7-5','Good'],['8-1','Good'],['9-1','Good'],['9-2','Good'],['9-3','Evil'],['9-4','Good'],['9-5','Good'],['10-1','Good'],['10-2','Good'],['10-3','Good'],['10-4','Evil'],['10-5','Good'],['11-1','Good']]

    return render_template('index.html', title="AFBOTC", goodvsevil = goodvsevil)