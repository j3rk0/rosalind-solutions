with open("data/rosalind_subs.txt") as f:
    io = f.readlines()
    x = io[0].replace('\n','')
    y = io[1].replace('\n','')

l = len(y)
res = []
for i in range(len(x)-l + 1):
    if x[i:i+l] == y:
        res.append(str(i+1))

res = " ".join(res)

with open('data/rosalind_subs_sub.txt', 'w') as f:
    f.write(res)
