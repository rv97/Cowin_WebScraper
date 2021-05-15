#!flask/bin/python
from utils import Cowinutils
from cowin_parser import CowinParser
from flask import Flask
from flask import request
from flask import abort
app = Flask(__name__)

searchDetails = {}
@app.route('/setSearch', methods=['POST'])
def setSearchQuery():
    response_text = {}
    if not request.json:
        abort(400)
    else:
        searchDetails = request.json
        response_text = "Request Placed Successfully."
        cowinParser = CowinParser()
        cowinParser.startProcess(searchDetails)
    return response_text, 201


@app.route('/')
def index():
    return "hello world"
if __name__ == '__main__':
    app.run(debug=True)