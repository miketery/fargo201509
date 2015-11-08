#!/usr/bin/python

from flask import Flask

app = Flask(__name__)
app.run(debug=True)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/getState/<states>')
def getState(states):
	inp=(" ").split(states)
	if inp[0] is "NOT":
		return "NOT"
	return states

if __name__ == '__main__':
    app.run(host='0.0.0.0')
