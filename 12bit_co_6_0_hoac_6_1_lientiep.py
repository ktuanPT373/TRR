def Try(i):
    global s,count
    for v in ('0','1'):
        s += v
        if i == 12:
            if  '000000' in s or '111111' in s:
                count += 1
        else:
            Try(i+1)
        s = s[:-1]
s = ''
count = 0
Try(1)
print(count)