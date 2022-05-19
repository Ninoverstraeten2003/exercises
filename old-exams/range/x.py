
with open('output.txt','w') as o:
    str = '\n'.join([str(i) for i in range(1,1000001)])
    o.write(f'{str}')