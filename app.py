from flask import Flask
from SearchStringUtility import SearchStringUtility
from DataCollection import DataCollection
from CSVFIleUtility import  CSVFileUtility
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
    csv_obj = CSVFileUtility()

    url_data = sc_obj.prepare_search_url()

    final_data = {}

    for each_key in url_data:
        print(each_key)
        final_data[each_key] = dc_obj.get_data(url_data[each_key])

    csv_obj.write_csv(final_data,'query.csv')

    # print(final_data)
    return json.dumps(final_data)

if __name__ == '__main__':
    app.run(debug = True)

