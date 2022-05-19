import re



def max_length_index_tuple(list,index):
    for i in list:
        yield((len(i[index])))
        
with open('input.txt') as f:
    with open('output.txt','w') as g:
        content = f.readlines()
        
        names_ip = [re.search(r'(\D*) (\d+.\d+.\d+.\d+) (.*)',i).groups() for i in content]
        
        
        maxnames = max(max_length_index_tuple(names_ip,0))
        maxip = max(max_length_index_tuple(names_ip,1))
        print(maxnames)

        for i in content:
            x = re.search(r'(\D*) (\d+.\d+.\d+.\d+) (.*)',i)
            
            i,j,k = x.groups()
            g.write(f"{i.rjust(maxnames,' ')} {j.ljust(maxip,' ')} {k.strip()}\n")
    
    
        

        
        
            
    
    

  
    