count = 0
for a in range(15):
    for b in range(15):
        for c in range(15):
            if a + 2*b + 5*c == 14:
                print(a,b,c)
                count += 1

print(count)
