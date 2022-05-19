
from distutils.dir_util import copy_tree
import json


with open('input.json','r') as j:
    content = json.load(j)
    

    content.sort(key=lambda x: x['score'],reverse=True)
    with open('output.txt','w') as w:
        for i,k in enumerate(content,start=1):
            w.write(f'{i} {k["name"]}\n')