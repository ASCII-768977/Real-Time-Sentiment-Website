# encoding:utf-8
# !/usr/bin/env python

from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit
from threading import Lock
import random
import couchdb
import time
import json
import ast

async_mode = None
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

socketio = SocketIO(app)
thread = None
thread_lock = Lock()


@app.route('/')
def home_page():
    global melHotTopic, melSentiment, sydHotTopic, sydSentiment, adeHotTopic, adeSentiment, briHotTopic, briSentiment, cbdHotTopic, cbdSentiment, preHotTopic, preSentiment, donHotTopic, donSentiment, SYHotTopic, SYSentiment
    melHotTopic = []
    melSentiment = []
    sydHotTopic = []
    sydSentiment = []
    adeHotTopic = []
    adeSentiment = []
    briHotTopic = []
    briSentiment = []
    cbdHotTopic = []
    cbdSentiment = []
    preHotTopic = []
    preSentiment = []
    donHotTopic = []
    donSentiment = []
    SYHotTopic = []
    SYSentiment = []
    return render_template('HomePage.html')


@app.route('/MapPage.html')
def map_page():
    return render_template('MapPage.html')


@app.route('/ChartPage.html')
def chart_page():
    return render_template('ChartPage.html')


@app.route('/refreshMel')
def refresh_mel():
    global melHotTopic, melSentiment, sydHotTopic, sydSentiment, adeHotTopic, adeSentiment, briHotTopic, briSentiment, cbdHotTopic, cbdSentiment, preHotTopic, preSentiment, donHotTopic, donSentiment, SYHotTopic, SYSentiment
    print("melHotTopic now: " + str(melHotTopic))
    print("melSentiment now: " + str(melSentiment))
    return jsonify(webTopic=melHotTopic, webSentiment=melSentiment, webTime=time.strftime('%M:%S', time.localtime()))


@app.route('/refreshSyd')
def refresh_syd():
    global melHotTopic, melSentiment, sydHotTopic, sydSentiment, adeHotTopic, adeSentiment, briHotTopic, briSentiment, cbdHotTopic, cbdSentiment, preHotTopic, preSentiment, donHotTopic, donSentiment, SYHotTopic, SYSentiment
    print("sydHotTopic now: " + str(sydHotTopic))
    print("sydSentiment now: " + str(sydSentiment))
    return jsonify(webTopic=sydHotTopic, webSentiment=sydSentiment, webTime=time.strftime('%M:%S', time.localtime()))


@app.route('/refreshAde')
def refresh_ade():
    global melHotTopic, melSentiment, sydHotTopic, sydSentiment, adeHotTopic, adeSentiment, briHotTopic, briSentiment, cbdHotTopic, cbdSentiment, preHotTopic, preSentiment, donHotTopic, donSentiment, SYHotTopic, SYSentiment
    print("adeHotTopic now: " + str(adeHotTopic))
    print("adeSentiment now: " + str(adeSentiment))
    return jsonify(webTopic=adeHotTopic, webSentiment=adeSentiment, webTime=time.strftime('%M:%S', time.localtime()))


@app.route('/refreshBri')
def refresh_bri():
    global melHotTopic, melSentiment, sydHotTopic, sydSentiment, adeHotTopic, adeSentiment, briHotTopic, briSentiment, cbdHotTopic, cbdSentiment, preHotTopic, preSentiment, donHotTopic, donSentiment, SYHotTopic, SYSentiment
    print("briHotTopic now: " + str(briHotTopic))
    print("briSentiment now: " + str(briSentiment))
    return jsonify(webTopic=briHotTopic, webSentiment=briSentiment, webTime=time.strftime('%M:%S', time.localtime()))


@app.route('/refreshCbd')
def refresh_cbd():
    global melHotTopic, melSentiment, sydHotTopic, sydSentiment, adeHotTopic, adeSentiment, briHotTopic, briSentiment, cbdHotTopic, cbdSentiment, preHotTopic, preSentiment, donHotTopic, donSentiment, SYHotTopic, SYSentiment
    print("cbdHotTopic now: " + str(cbdHotTopic))
    print("cbdSentiment now: " + str(cbdSentiment))
    return jsonify(webTopic=cbdHotTopic, webSentiment=cbdSentiment, webTime=time.strftime('%M:%S', time.localtime()))


@app.route('/refreshPre')
def refresh_pre():
    global melHotTopic, melSentiment, sydHotTopic, sydSentiment, adeHotTopic, adeSentiment, briHotTopic, briSentiment, cbdHotTopic, cbdSentiment, preHotTopic, preSentiment, donHotTopic, donSentiment, SYHotTopic, SYSentiment
    print("preHotTopic now: " + str(preHotTopic))
    print("preSentiment now: " + str(preSentiment))
    return jsonify(webTopic=preHotTopic, webSentiment=preSentiment, webTime=time.strftime('%M:%S', time.localtime()))


@app.route('/refreshDon')
def refresh_don():
    global melHotTopic, melSentiment, sydHotTopic, sydSentiment, adeHotTopic, adeSentiment, briHotTopic, briSentiment, cbdHotTopic, cbdSentiment, preHotTopic, preSentiment, donHotTopic, donSentiment, SYHotTopic, SYSentiment
    print("donHotTopic now: " + str(donHotTopic))
    print("donSentiment now: " + str(donSentiment))
    return jsonify(webTopic=donHotTopic, webSentiment=donSentiment, webTime=time.strftime('%M:%S', time.localtime()))


@app.route('/refreshSY')
def refresh_SY():
    global melHotTopic, melSentiment, sydHotTopic, sydSentiment, adeHotTopic, adeSentiment, briHotTopic, briSentiment, cbdHotTopic, cbdSentiment, preHotTopic, preSentiment, donHotTopic, donSentiment, SYHotTopic, SYSentiment
    print("SYHotTopic now: " + str(SYHotTopic))
    print("SYSentiment now: " + str(SYSentiment))
    return jsonify(webTopic=SYHotTopic, webSentiment=SYSentiment, webTime=time.strftime('%M:%S', time.localtime()))


@app.route('/updateMel', methods=['POST'])
def update_mel():
    global melHotTopic, melSentiment, sydHotTopic, sydSentiment, adeHotTopic, adeSentiment, briHotTopic, briSentiment, cbdHotTopic, cbdSentiment, preHotTopic, preSentiment, donHotTopic, donSentiment, SYHotTopic, SYSentiment
    if not request.form or 'avgSentiment' not in request.form:
        return "error", 400
    melHotTopic = ast.literal_eval(request.form["hotTopics"])
    melSentiment = ast.literal_eval(request.form["avgSentiment"])
    print("melHotTopic received: " + str(melHotTopic))
    print("melSentiment received: " + str(melSentiment))
    return "success", 201


@app.route('/updateSyd', methods=['POST'])
def update_syd():
    global melHotTopic, melSentiment, sydHotTopic, sydSentiment, adeHotTopic, adeSentiment, briHotTopic, briSentiment, cbdHotTopic, cbdSentiment, preHotTopic, preSentiment, donHotTopic, donSentiment, SYHotTopic, SYSentiment
    if not request.form or 'avgSentiment' not in request.form:
        return "error", 400
    sydHotTopic = ast.literal_eval(request.form["hotTopics"])
    sydSentiment = ast.literal_eval(request.form["avgSentiment"])
    print("sydHotTopic received: " + str(sydHotTopic))
    print("sydSentiment received: " + str(sydSentiment))
    return "success", 201


@app.route('/updateAde', methods=['POST'])
def update_ade():
    global melHotTopic, melSentiment, sydHotTopic, sydSentiment, adeHotTopic, adeSentiment, briHotTopic, briSentiment, cbdHotTopic, cbdSentiment, preHotTopic, preSentiment, donHotTopic, donSentiment, SYHotTopic, SYSentiment
    if not request.form or 'avgSentiment' not in request.form:
        return "error", 400
    adeHotTopic = ast.literal_eval(request.form["hotTopics"])
    adeSentiment = ast.literal_eval(request.form["avgSentiment"])
    print("briHotTopic received: " + str(adeHotTopic))
    print("adeSentiment received: " + str(adeSentiment))
    return "success", 201


@app.route('/updateBri', methods=['POST'])
def update_bri():
    global melHotTopic, melSentiment, sydHotTopic, sydSentiment, adeHotTopic, adeSentiment, briHotTopic, briSentiment, cbdHotTopic, cbdSentiment, preHotTopic, preSentiment, donHotTopic, donSentiment, SYHotTopic, SYSentiment
    if not request.form or 'avgSentiment' not in request.form:
        return "error", 400
    briHotTopic = ast.literal_eval(request.form["hotTopics"])
    briSentiment = ast.literal_eval(request.form["avgSentiment"])
    print("briHotTopic received: " + str(briHotTopic))
    print("briSentiment received: " + str(briSentiment))
    return "success", 201


@app.route('/updateCbd', methods=['POST'])
def update_cbd():
    global melHotTopic, melSentiment, sydHotTopic, sydSentiment, adeHotTopic, adeSentiment, briHotTopic, briSentiment, cbdHotTopic, cbdSentiment, preHotTopic, preSentiment, donHotTopic, donSentiment, SYHotTopic, SYSentiment
    if not request.form or 'avgSentiment' not in request.form:
        return "error", 400
    cbdHotTopic = ast.literal_eval(request.form["hotTopics"])
    cbdSentiment = ast.literal_eval(request.form["avgSentiment"])
    print("cbdHotTopic received: " + str(cbdHotTopic))
    print("cbdSentiment received: " + str(cbdSentiment))
    return "success", 201


@app.route('/updatePre', methods=['POST'])
def update_pre():
    global melHotTopic, melSentiment, sydHotTopic, sydSentiment, adeHotTopic, adeSentiment, briHotTopic, briSentiment, cbdHotTopic, cbdSentiment, preHotTopic, preSentiment, donHotTopic, donSentiment, SYHotTopic, SYSentiment
    if not request.form or 'avgSentiment' not in request.form:
        return "error", 400
    preHotTopic = ast.literal_eval(request.form["hotTopics"])
    preSentiment = ast.literal_eval(request.form["avgSentiment"])
    print("preHotTopic received: " + str(preHotTopic))
    print("preSentiment received: " + str(preSentiment))
    return "success", 201


@app.route('/updateDon', methods=['POST'])
def update_don():
    global melHotTopic, melSentiment, sydHotTopic, sydSentiment, adeHotTopic, adeSentiment, briHotTopic, briSentiment, cbdHotTopic, cbdSentiment, preHotTopic, preSentiment, donHotTopic, donSentiment, SYHotTopic, SYSentiment
    if not request.form or 'avgSentiment' not in request.form:
        return "error", 400
    donHotTopic = ast.literal_eval(request.form["hotTopics"])
    donSentiment = ast.literal_eval(request.form["avgSentiment"])
    print("donHotTopic received: " + str(donHotTopic))
    print("donSentiment received: " + str(donSentiment))
    return "success", 201


@app.route('/updateSY', methods=['POST'])
def update_SY():
    global melHotTopic, melSentiment, sydHotTopic, sydSentiment, adeHotTopic, adeSentiment, briHotTopic, briSentiment, cbdHotTopic, cbdSentiment, preHotTopic, preSentiment, donHotTopic, donSentiment, SYHotTopic, SYSentiment
    if not request.form or 'avgSentiment' not in request.form:
        return "error", 400
    SYHotTopic = ast.literal_eval(request.form["hotTopics"])
    SYSentiment = ast.literal_eval(request.form["avgSentiment"])
    print("SYHotTopic received: " + str(SYHotTopic))
    print("SYSentiment received: " + str(SYSentiment))
    return "success", 201


if __name__ == '__main__':
    print('done')
    socketio.run(app, debug=True)
    #socketio.run(app, host='0.0.0.0', port=80, debug=True)
