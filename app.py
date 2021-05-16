#!flask/bin/python
from logging import debug
from startProcess import startThread, registerNotification
from flask import Flask
from flask import request
from flask import abort

app = Flask(__name__)

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

@app.route('/registerNotify', methods=['GET'])
def notificationRegistration():
    result = registerNotification()
    return result, 201

@app.route('/')
def index():
    return "Welcome to Cowin Notifier"

if __name__ == '__main__':
    app.run(threading=True)