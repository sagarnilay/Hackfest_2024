import json 

json_values = [
    
        {"ID" : 1,  "Status":"Open", "Severity": "Important", "Description": "descript1", "Title": "title1"},
        {"ID" : 2,  "Status":"Closed", "Severity": "Important", "Description": "descript2", "Title": "title2"}, 
        {"ID" : 3,  "Status":"Closed", "Severity": "Important", "Description": "descript3", "Title": "title3"},
        {"ID" : 4,  "Status":"Open", "Severity": "Unimportant", "Description": "descript4", "Title": "title4"}
    
]    

with open('json_data.json', 'w') as outfile:
    json.dump(json_values, outfile)