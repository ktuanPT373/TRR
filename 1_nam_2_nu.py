# co bao nhieu cach chon 1 nam tu 10 nam va 2 nu tu 15 nu
count = 0
for i in range(0,10):
    for j in range(0,15):
        for k in range(j+1,15):
            count += 1

print(count)