import os
import json
import csv

class CSVFileUtility:
    def __init__(self):
        pass

    def write_header(self, json_data, file_obj):
        count = 0
        for each_search_key in json_data:
            single_search_data = json_data[each_search_key]
            output = csv.writer(file_obj)
            for each_record in single_search_data:
                if count < 1:
                    header = list(each_record)
                    header.append('search-term')
                    output.writerow(header)
                    count = count + 1


    def write_rows(self, json_data, file_path):

        for each_search_key in json_data:
            try:
                single_search_data = json_data[each_search_key]
                file_obj = open(file_path, "a")
                output = csv.writer(file_obj)
                for each_record in single_search_data:
                    row = list(each_record.values())
                    row.append(each_search_key)
                    output.writerow(row)
            except Exception:
                print('Error in Writing')

    def write_csv(self, json_data, filename):
        directory_path = "data/"
        file_path = directory_path+filename

        if os.path.exists(file_path):
            print("File Exists. Append it")
            self.write_rows(json_data,file_path)

        else:
            file_obj = open(file_path, "w+")
            print("New File Created")
            self.write_header(json_data, file_obj)
            self.write_rows(json_data,file_path)






