import urllib.request as request
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello world"

@app.route('/api', methods = ['GET'])
def hello_world():
    A = 2
    return str(A)

#To run use flask run
if __name__ == "__main__":
    app.run()