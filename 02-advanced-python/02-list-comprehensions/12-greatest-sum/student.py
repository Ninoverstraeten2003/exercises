      

def greatest_sum(ns):
    l = range(len(ns))
    c = [(ns[i:j+1],i,j+1) for i in l for j in l]
    return (max([(sum(n),i,j) for n,i,j in c],key = lambda x : x[0])[1:])
   

print(greatest_sum([1]))

    
    
    

    
    
    
    
    