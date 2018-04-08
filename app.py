from flask import Flask
from SearchStringUtility import SearchStringUtility
from DataCollection import DataCollection
from CSVFIleUtility import  CSVFileUtility
import json
from time import sleep
import datetime

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/data', methods = ['GET'])
def sample_data():
    return 'Hello Data'

@app.route('scrape/data/', methods=['GET'])
def scrape_data(start_date):

    csv_obj = CSVFileUtility()
    return json.dumps('hello')

if __name__ == '__main__':
    app.run(debug = True)

