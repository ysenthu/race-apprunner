
# ==========================================
#  Title:  Flask Simple API
#  Author: Senthu
#  Date:   30 May 2021
# ==========================================

from flask import Flask, jsonify
from flask import request,abort
from datetime import datetime
from warnings import WarningMessage
import urllib.request as urllib
import logging

app = Flask(__name__)
app.logger.setLevel(logging.DEBUG)
@app.errorhandler(500)
def general_application_error(e):
    """ General Error Hanlder
        returns 500 on invocation
    """
    return jsonify(error=str(e)), 500

@app.route('/')
def appRoot():
    now = datetime.now()

    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

    return jsonify({"message": "Hello From Senthu's Flask App, Current Date is : {} ".format(dt_string)})

@app.route('/greeting')
def healthcheck():
    now = datetime.now()

    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

    return jsonify({"message": "Hello From Senthu's Flask App, Current Date is : {} ".format(dt_string)})

def main():
    app.run(debug=False, host='0.0.0.0',port=8765)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0',port=8765)
