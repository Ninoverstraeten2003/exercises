import imghdr
with open('output.txt', 'w') as f:
    for i in range(1,101):
        with open(f"{i}.unknown",'rb') as u:
            filetype = imghdr.what(u)
            f.write(f"mv {i}.unknown {i}.{filetype}\n")
            
            