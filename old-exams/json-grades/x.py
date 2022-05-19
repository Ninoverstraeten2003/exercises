import json
from pprint import pprint


with open('input.json', 'r') as f:
    with open('output.txt', 'w') as out:
        content = json.load(f)
        content.sort(key=lambda x: list(x.items())[0][1])
        for i in content:
            id,grades = i.items()
            out.write(f"{id[1]} {round(sum(grades[1])/len(grades[1]))}\n")
            
                
        
    