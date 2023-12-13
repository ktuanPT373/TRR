import time
start = time.time()
# how many 5 digit numbers abcde are there so that a < b < c < d > e or a > b > c > e > e ?
# def ok(s):
#     lis = [int(digit) for digit in str(s)]
#     a,b,c,d,e = lis
#     if a < b < c < d < e or a > b > c > d > e:
#         return True
#     return False
# count = 0
# for s in range(10000,100000):
#     if ok(s):
#         count +=1
count = 0
for a in range(1,10):
    for b in range(0,10):
        for c in range(0,10):
            for d in range(0,10):
                for e in range(0,10):
                    if a > b > c > d > e or a < b < c < d < e:
                        count += 1
print(count)
end = time.time()
print('time:',end-start)