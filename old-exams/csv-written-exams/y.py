import csv 
"""Lector,Lector Naam,Lector Voornaam,Datum,Startuur,Dagdeel,OLA Code,OLA Naam,Semester,Ex. Soortx,Reeks Info,Student ID,Lokaal"""
with open('exam-schedule.csv','r') as f:
    with open('output.txt', 'w') as g:
        content = csv.DictReader(f)
        s = []
        d = dict()
        s = [row for row in content if row["Ex. Soortx"] == 'S']
        
       
    
            
        for i in s:
            lectors = i["Lector"].split('/')
            if len(lectors) > 1:
                for lector in lectors:
                    d[lector] = d.get(lector,0) + 1
            else:      
                d[i["Lector"]] = d.get(i["Lector"],0) + 1
        
        d = dict(sorted(d.items(), key=lambda x : x[0]))
        
        for i,j in d.items():
            g.write(f"{i} {j}\n")
            
            