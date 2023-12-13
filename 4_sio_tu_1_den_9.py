# Co bao nhieu cach chon ra 4 so tu 1 den 8 sao cho luon co hai so lien tiep nhau cung duoc chon
count = 0
for a in range(1,9):
    for b in range(a+1,9):
        for c in range(b+1,9):
            for d in range(c+1,9):
                if abs(a-b) == 1 or abs(a-c) == 1 or abs(a-d) == 1 or abs(b-c) == 1 or abs(b-d) == 1 or abs(c-d) == 1:
                    # print(a,b,c,d)
                    count += 1
print(count)   