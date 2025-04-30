import csv
import json


csv_filepath = "atp_tennis.csv"
json_filepath = "atp_tennisJSON.json"


data_dict = []
with open(csv_filepath, mode='r', encoding='latin1') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    for row in csv_reader:
        cleaned_row = {key.strip(): value.strip() for key, value in row.items()}
        data_dict.append(cleaned_row)
    
data_final = {'docs': data_dict}

with open(json_filepath, mode='w', encoding='utf-8') as jsonfile:
    json.dump(data_final, jsonfile, indent=4, ensure_ascii=False)