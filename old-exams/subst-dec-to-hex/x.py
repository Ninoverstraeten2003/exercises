import re 
        
def he(match): 
    x = int(match.group(1))
    return rf'{hex(x)}'

with open('input.txt', 'r') as f:
    with open('output.txt', 'w') as g:
        content = f.read()
        
        content = re.sub(r'\$HEX\((\d+)\)',he,content)
    
   
        g.write(content)
