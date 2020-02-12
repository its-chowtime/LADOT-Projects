# Tutorial from https://www.makeuseof.com/tag/python-javascript-communicate-json/

from flask import Flask

app = Flask(__name__)

@app.route("/output")
def output():
    return "Hello World!"

if __name__ == "__main__":
    app.run()
