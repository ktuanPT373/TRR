# co bao nhieu xau nhi phan do dai 6 k chua hai bit 1 dung canh nhau 
count = 0
strin = ''
bits = ('0','1')
def Try(i):
    global strin,count
    for v in bits:
        strin += v
        if len(strin) == 6:
            if '11' not in strin:
                print(strin)
                count += 1
        else:
            Try(i+1)
        strin = strin[:-1]
Try(0)
print(count)
