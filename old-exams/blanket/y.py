import json
from datetime import datetime
from statistics import mean

with open("input.txt", "r") as f:
    d = json.load(f)
    
    d = dict(sorted(d.items(), key=lambda x : datetime.strptime(x[0],'%d/%m/%Y')))
    
    for k,v in d.items():
        d[k] = round(mean(v))

    with open("output.txt", "w") as f:
        for k,v in d.items():
            f.write(f"{v}\n")
    
    
    
    
    