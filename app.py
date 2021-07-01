from flask import Flask, Response
app = Flask(__name__)

def status200():
	status_code = Response(status=200)
	return status_code

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/status")
def health():
	print(status200())
	return "result: OK - healthy"

@app.route("/metrics")
def metrics():
	print(status200())
	return "data: {UserCount: 140, UserCountActive: 23}"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
