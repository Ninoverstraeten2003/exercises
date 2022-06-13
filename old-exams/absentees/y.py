


with open('all.txt', 'r') as f:
    all = [i.strip().lower() for i in f.readlines()]
    with open('attending.txt', 'r') as f:
        attending = [i.strip().lower() for i in f.readlines()]
        absentees = [i for i in all if i not in attending]
        with open('absentees.txt', 'w') as f:
            for i in absentees:
                f.write(f"{i}\n")
        
    



    
    