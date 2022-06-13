morse = {
"A":".-"
,"B":"-..."
,"C":"-.-."
,"D":"-.."
,"E":"."
,"F":"..-."
,"G":"--."
,"H":"...."
,"I":".."
,"J":".---"
,"K":"-.-"
,"L":".-.."
,"M":"--"
,"N":"-."
,"O":"---"
,"P":".--."
,"Q":"--.-"
,"R":".-."
,"S":"..."
,"T":"-"
,"U":"..-"
,"V":"...-"
,"W":".--"
,"X":"-..-"
,"Y":"-.--"
,"Z":"--.."
}

"""Write two functions (yes, two!) to_morse(string) and from_morse(string) that convert to and from morse, respectively. Below are the codes for each letter.

In Morse code, letters are separated by one space and words by three spaces. For example, I AM is written
..   .- --
  ^^^  ^
  """
antimorse = dict([(x,y) for y,x in morse.items()])


def to_morse(string):
    words = string.upper().split(' ')
    morse_words = []
    for word in words:
        letters = [i for i in word]
        morse_letters = [morse[i] for i in letters]
        morse_words.append(' '.join(morse_letters))
    return '   '.join(i for i in morse_words)
    

def from_morse(string):
    words = string.split('   ')

    txt_words = []

    for word in words:
        morse_letters = word.split(' ')
        letters = [antimorse[i] for i in morse_letters]
        txt_words.append(''.join(letters))
    return ' '.join(i for i in txt_words)

print(from_morse("..   .- --"))
    
    
