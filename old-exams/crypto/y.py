

import json


with open('input.json', 'r') as f:
    with open('output.txt', 'w') as g:
        d = json.load(f)
        
        for i in d:
            currency = i["currency"]
            minimum = min(i["history"])
            maximum = max(i["history"])
            current = i["history"][-1]
            
            g.write(f"{currency} {minimum} {maximum} {current}\n")
            

    