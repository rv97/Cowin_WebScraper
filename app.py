#!flask/bin/python
from logging import debug
from startProcess import startThread, registerNotification
from flask import Flask, render_template
from flask import request
from flask import abort
from utils import Cowinutils

app = Flask(__name__)
cowinUtils = Cowinutils()

@app.route('/registerNotify', methods=['GET'])
def notificationRegistration():
    result = registerNotification()
    return result, 201

@app.route('/getStates', methods=["GET"])
def getStates():
    cowinUtils.getStates()
    return cowinUtils.STATES_JSON, 201

@app.route('/getDistrict/<state_id>', methods=["GET"])
def getDistricts(state_id):
    cowinUtils.getDistrict(state_id)
    return cowinUtils.DISTRICTS, 201

@app.route('/setSearch', methods=['POST'])
def setSearchQuery():
    response_text = {}
    if not request.json:
        abort(400)
    else:
        searchDetails = request.json
        response_text = "Request Placed Successfully."
        startThread(searchDetails)
    return response_text, 201


@app.route('/')
def index():
    return render_template('swaggerui.html')

if __name__ == '__main__':
    app.run(threading=True)