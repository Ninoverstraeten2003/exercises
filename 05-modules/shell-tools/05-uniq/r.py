"""uniq optionally takes a filename as command line argument. If no such argument is provided, it will read its input from STDIN.
The flag --ignore-case (or -i for short) should compare lines without taking case into account."""

import argparse
import sys

parser = argparse.ArgumentParser(prog='read')
parser.add_argument('file', help='File')
parser.add_argument('--ignorecase','-i', help='Ignore case', default=False, action='store_true')


args = parser.parse_args()

file = args.file
ignore = args.ignorecase

if not file:
    file = sys.stdin
    
with open(file, 'r') as f:
    contents = f.readlines()
    if not ignore:
        q = list(set([line.strip() for line in contents]))
        print(q)
        
    else:
        upper = [line.strip().upper() for line in contents]
        c = list(set(upper))
        result = set()
        for i in [line.strip() for line in contents]:
            for j in c:
                if(i.upper() == j):
                    result.add(i)
        for i in result:
            print(i)
                    

        
    
         
