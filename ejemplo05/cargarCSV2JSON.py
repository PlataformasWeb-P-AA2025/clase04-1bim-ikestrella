import csv
import json

# Rutas de los archivos
# A leer
csv_filepath = "atp_tennis.csv"
# JSON de salida
json_filepath = "atp_tennisJSON.json"

# Lista donde va a estar los datos del csv en formato dictionary 
data_dict = []
with open(csv_filepath, mode='r', encoding='latin1') as csvfile:
    # Lee el csv
    csv_reader = csv.DictReader(csvfile)
    # Itera cada fila del csv
    for row in csv_reader:
        # Coloca en el forato de clave valor
        cleaned_row = {key.strip(): value.strip() for key, value in row.items()}
        # Lo agrega a la lista creada previamente con el formato ya hecho
        data_dict.append(cleaned_row)

# Se coloca en el formato para poder subirlo a coachDB
data_final = {'docs': data_dict}

# Escribe el data_final con el formato correcto
with open(json_filepath, mode='w', encoding='utf-8') as jsonfile:
    json.dump(data_final, jsonfile, indent=4, ensure_ascii=False)