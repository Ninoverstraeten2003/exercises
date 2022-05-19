with open('output.txt','w') as out:
    for i in range(10001):
        out.write(f'{str(i).rjust(10)}{str(bin(i)).rjust(20)}{str(hex(i)).rjust(10)}\n')
    
