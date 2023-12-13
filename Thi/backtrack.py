def condition():
    return True
    
def Try(i):
    global s,count,n
    for v in range(1,10):
        if v not in visited:
            s[i] = v
            visited.add(v)
            if i == n-1:
                if condition():
                    #print(s)
                    count += 1
            else:
                Try(i+1)
            s[i] = -1
            visited.remove(v)
n = 9 # number of bits here
s = [-1]*n
visited = set()
count = 0 
Try(0)
print(count)