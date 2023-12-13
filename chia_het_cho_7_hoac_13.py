count = 0 
for i in range(1,2002):
    if i%7==0 or i%13==0:
        count += 1
print(count)