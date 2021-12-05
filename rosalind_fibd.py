with open('data/rosalind_fibd.txt') as f:
    n, m = f.readline().replace('\n', '').split(' ')

n = int(n)
m = int(m)

rabbits = [0] * m
rabbits[0] = 1

for i in range(1, n):
    offspring = 0
    for j in reversed(range(1, m)):
        offspring += rabbits[j]
        rabbits[j] = rabbits[j - 1]
    rabbits[0] = offspring

print(f"rabbits after {n} month: {sum(rabbits)}")
