count = 0
s,e = 1,14
for x1 in range(s,e+1):
    for x2 in range(s,e+1):
        for x3 in range(s,e+1):
            for x4 in range(s,e+1):
                # for x5 in range(s,e+1):
                #     for x6 in range(s,e+1):
                #         for x7 in range(s,e+1):
                #             for x8 in range(s,e+1):
                #                 for x9 in range(s,e+1):
                #                     for x10 in range(s,e+1):
                #                         for x11 in range(s,e+1): 
                                            # write what you want into this
                                            if x1 + x2 + x3 + x4 == 14:
                                                print(x1,x2,x3,x4)
                                                count += 1
print(count)


