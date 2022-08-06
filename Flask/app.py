import urllib.request as request
from flask import Flask
import AllFunctions 

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello world"

@app.route('/api', methods = ['GET'])
def hello_world():
    AllFunctions.selectCategory("Phones")
    AllFunctions.checkDevice("Samsung galaxy s6")
    AllFunctions.selectDevice("Samsung galaxy s6")
    print(AllFunctions.chackPrice())

    A = 2
    return str(A)

#To run use flask run
if __name__ == "__main__":
    app.run()