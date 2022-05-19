
with open('input.txt') as f:
    with open('output.txt','w') as g:
        content = [i.strip() for i in f.readlines()]
        times = int(len(content)/100)
        name_score = []
        index = 0
        for i in range(times):
            for j in range(100,0,-1):
                name_score.append((content[index],j))
                index += 1
                
        result = dict()
        for name,score in name_score:
            result[name] = result.get(name,0) + score
        end_result = list(result.items())
        end_result.sort(key=lambda x: x[1],reverse=True)
        for i,j in end_result[:10]:
            g.write(f'{i}\n')
        
        