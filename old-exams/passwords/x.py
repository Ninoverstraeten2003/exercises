import itertools
import re

length = 6
letters = "QWERTYUIOP"
vowels = [i for i in "AEIOU"]
consonant = [i for i in "QWRTYP"]

def generate_strings(length=6):
    chars = "QWERTYUIOP"
    for item in itertools.product(sorted(chars), repeat=length):
        yield "".join(item)


with open('output.txt', 'w') as output:
    sol = []
    for i in generate_strings():
        pwd = ''.join(i)
        if re.search(fr'([{"".join(consonant)}])\1', pwd) and re.search(fr'([{"".join(vowels)}])\1', pwd) and len(set(pwd)) == 4:
            output.write(f"{''.join(i)}\n")



