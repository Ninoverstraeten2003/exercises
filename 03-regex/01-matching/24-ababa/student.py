# Write your code here
import imp


import re

def ababa(string):
    return re.fullmatch(r'(.+)(.+)\1\2\1',string)