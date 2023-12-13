take = 'ABCDE1234'
count = 0
for a in take:
    for b in take:
        if a in 'ABCDE' or b in 'ABCDE':
            print(a,b)
            count += 1
print(count)
