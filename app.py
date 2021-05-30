
# ==========================================
#  Title:  Flask Simple API
#  Author: Senthu
#  Date:   30 May 2021
# ==========================================

from flask import Flask, jsonify,abort
from datetime import datetime
import logging,os

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

@app.route('/healthz')
def healthcheck():
    now = datetime.now()

    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

    return jsonify({"message": "Hello From Senthu's Flask App, Current Date is : {} ".format(dt_string)})


if __name__ == "__main__":

    if os.getenv('ENVIRONMENT') is not None:
        app.config['environment'] = os.getenv('ENVIRONMENT')
    else:
        app.config['environment'] = "dev"

    app.run(debug=False, host='0.0.0.0',port=8888)