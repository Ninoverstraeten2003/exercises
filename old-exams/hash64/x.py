import hashlib
import base64

with open('output.txt', 'w') as f:
    for i in range(10001):
        str_num = str(i)
        byt_num = bytes(str_num,encoding="ascii")
        m = hashlib.sha384()
        m.update(byt_num)
        base64_bytes = base64.b64encode(m.digest())
        base64_message = base64_bytes.decode('ascii')
        f.write(f"{i} {base64_message}\n")
    
    
    
   
