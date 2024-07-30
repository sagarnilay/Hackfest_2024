import json 

json_values = [
    
        {"ID" : 1,  "Status":"Open", "Severity": "Important", "Description": "descript1", "Title": "title1"},
        {"ID" : 2,  "Status":"Open", "Severity": "Important", "Description": "descript1", "Title": "title1"}, 
        {"ID" : 3,  "Status":"Open", "Severity": "Important", "Description": "descript1", "Title": "title1"}
    
]    

with open('json_data.json', 'w') as outfile:
    json.dump(json_values, outfile)