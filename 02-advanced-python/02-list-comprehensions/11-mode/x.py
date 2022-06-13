def mode(ns):
    result = dict()
    for i in ns:
        result[i] = result.get(i,0) + 1
    return sorted(result.items(),key=lambda x: x[1], reverse=True)[0][0]



