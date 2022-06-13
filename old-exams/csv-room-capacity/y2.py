import csv
"""Lector,Lector Naam,Lector Voornaam,Datum,Startuur,Dagdeel,OLA Code,OLA Naam,Semester,Ex. Soortx,Reeks Info,Student ID,Lokaal"""
"""U0100800,Appeltans,Karine,01-09-18,09:00,vm,MBK04a,Supply Chain Management,1,S,2MKC/CO,R0457616,D0.60 (Hemisfeer)"""

with open('exam-schedule.csv','r') as f:
    with open('output.txt', 'w') as g:
        content = csv.DictReader(f)
        s = []
        d = dict()
        for row in content:
            Datum = row["Datum"]
            Dagdeel = row["Dagdeel"]
            Lokaal = row["Lokaal"]
            
            s.append((Lokaal,Datum,Dagdeel))
        for i in s:
            d[i] = d.get(i,0) + 1
        
        d = dict(sorted(d.items(),key=lambda x: (x[0][0],x[1])))
        
        q = dict()
        for i,j in d.items():
            q[i[0]] = j

        for i,j in q.items():
            g.write(f"{i} {j}\n")
            
            
        
        
        
        
        