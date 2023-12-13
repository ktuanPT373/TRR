def condition():
    return '000000' in s or '111111' in s
    pass
    
def Try(i):
    global s,count,n
    for v in ('0','1'):
        s += v
        if i == n:
            if condition():
                #print(s)
                count += 1
        else:
            Try(i+1)
        s = s[:-1]
s = ''
n = 12 # number of bits here
count = 0 
Try(1)
print(count)