count = 0
for x1 in range(1,11):
    for x2 in range(1,11):
        for x3 in range(1,11):
            for x4 in range(1,11):
                if x1 + x2 + x3 + x4 == 10:
                    count += 1
print(count)




