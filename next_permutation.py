visited = set()
s = [-1]*9
def Try(i):
    global s,count,visited
    for v in range(1,10):
        if v not in visited:
            s[i] = v
            visited.add(v)
            if i == 8:
                if s[0] == 3 and s[1] == 8:
                    print(s)
            else:
                Try(i+1)
            s[i] = -1
            visited.remove(v)
Try(0)