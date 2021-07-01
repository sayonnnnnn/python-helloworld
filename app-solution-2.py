from flask import Flask
from flask import json
import logging

app = Flask(__name__)

@app.route('/status')
def healthcheck():
    response = app.response_class(
            response=json.dumps({"result":"OK - healthy"}),
            status=200,
            mimetype='application/json'
    )

    # app.logger.info () passes the following string when the particular route has been invoked by the
    # user in the browser session. 
    app.logger.info('Status request successfull')
    return response

@app.route('/metrics')
def metrics():
    response = app.response_class(
            response=json.dumps({"status":"success","code":0,"data":{"UserCount":140,"UserCountActive":23}}),
            status=200,
            mimetype='application/json'
    )

    ## log line
    app.logger.info('Metrics request successfull')
    return response

@app.route("/")
def hello():
    
    # app.logger.info () passes the following string when the particular route has been invoked by the
    # user in the browser session. 
    app.logger.info('Main request successfull')

    return "Hello World!"

if __name__ == "__main__":

    # logging is a library in Python which is used to separate out all the logger.info() 
    # in a separate file. 
    # In this case, logging.basicConfig() takes two arguments namely filename and level
    # filename --> Is the name of the file where all the logs of the flask app are stored in one place.
    # level --> Is the argument which enables the logging function to log only those requests if the log is of DEBUG level.
    logging.basicConfig(filename='app.log',level=logging.DEBUG)

    app.run(host='0.0.0.0')