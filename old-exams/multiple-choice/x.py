import csv
from re import I

with open('solutions.csv') as sol:
    reader = csv.reader(sol)
    solution = next(reader)
    
with open('answers.csv') as ans:
    with open('output.txt','w') as out:
        reader = csv.reader(ans)
        for row in reader:
            name = row[0]
            answers = row[1:]
            correct = 0
            for index,s in enumerate(solution):
                if answers[index] == s:
                    correct += 1
            out.write(f'{name} {correct}\n')
                
            
            
            
        

    

