#co bao nhieu bit co 4 ky tu va ky tu dau bang ky tu cuoi
count = 0
for a in range(0,2):
    for b in range(0,2):
        for c in range(0,2):
            for d in range(0,2):
                if a == d:
                    count += 1
print(count)
