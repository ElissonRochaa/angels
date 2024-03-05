import logging
from flask import Flask, request
from flask import jsonify
import datetime
import decimal
import json

from service import basic_service, complementary_service

from flask_cors import CORS

app = Flask(__name__)

"""
CORS function is to avoid No 'Access-Control-Allow-Origin' error
"""
CORS(app)

@app.route('/')
def hello():
    """webserice test method
    """
    return 'Welcome to MODELS API', 200


if __name__ == '__main__':
    # This is used when running locally. Gunicorn is used to run the
    #app.run(host='192.168.0.58', port=8080, debug=True, processes=4, threaded=True)
    #app.run(threaded=True,debug=True)
    #model = Model()
    app.run(host='0.0.0.0', port=5000)
## [END app]
