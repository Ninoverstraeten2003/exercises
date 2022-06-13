import re

with open("input.txt", "r") as f:
    with open("output.txt", "w") as g:
        for line in f:
            match = re.match(r'(.*):(\d+)/(\d+)(.*)', line.strip())
            if match:
                name,spend,earned,add = match.groups()
                earned = int(earned)
                spend = int(spend)
                earned +=  add.strip().count('+')
                spend +=  add.strip().count('-')
                g.write(f"{name}:{spend}/{earned}\n")