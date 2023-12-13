# xet tap (x1,x2,x3,x4) sao cho x1 + x2 + x3 + x4 = 14. hoi theo thu tu bo tiep theo cua (3,5,3,3) la bo nao
for x1 in range(0,15):
    for x2 in range(0,15):
        for x3 in range(0,15):
            for x4 in range(0,15):
                if x1 + x2 + x3 + x4 == 14:
                    print((x1,x2,x3,x4))