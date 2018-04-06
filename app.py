from flask import Flask
from SearchStringUtility import SearchStringUtility
import datetime
# from .SearchStringUtility import SearchStringUtility


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/data', methods = ['GET'])
def sample_data():
    return 'Hello Data'

@app.route('/data/<start_date>', methods=['GET'])
def scrape_data(start_date):
    sc_obj = SearchStringUtility()
    url_data = sc_obj.prepare_search_url()


    return 'Scrapping data for %s' %data


