import re
with open('input.md') as f:
    with open('output.txt','w') as g:
        content = f.read()
        content = re.sub('#','=',content)
        
        def replace(match):
            return '*' * int((len(match.group(1))/2)) +'*'
        content = re.sub(r'( *)\*',replace,content)
        g.write(content)
    
        
