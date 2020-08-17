import csv 
import json 
  

def make_json(csvFilePath, jsonFilePath):
    data = {} 
      
    with open(csvFilePath, encoding='utf-8') as csvf: 
        csvReader = csv.DictReader(csvf) 
        for rows in csvReader: 
            key = rows['Station']+rows['Latitude']+rows['Longitude']+rows['Date']
            data[key] = rows 
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf: 
        jsonf.write(json.dumps(data, indent=4)) 
csvFilePath = r'monthlyData.csv'
jsonFilePath = r'monthlyData.json'
make_json(csvFilePath, jsonFilePath)
