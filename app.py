from flask import Flask
from SearchStringUtility import SearchStringUtility
from DataCollection import DataCollection
import json
import datetime



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
    dc_obj = DataCollection()
    url_data = sc_obj.prepare_search_url()
    # print(url_data)
    final_data = {}

    for each_key in url_data:
        print(each_key)
        final_data[each_key] = dc_obj.get_data(url_data[each_key])


    # print(final_data)
    return json.dumps(final_data)


