with open('data/rosalind_fib.txt') as f:
    n_r, k_r = f.readline().replace('\n', '').split(' ')

n_r = int(n_r)
k_r = int(k_r)


def fib_rabbits(n, k):  # return number of rabbits and the offspring
    if n == 1:  # base case
        return 1, 0
    else:  # recursive case
        adults, offspring = fib_rabbits(n - 1, k)
        return adults + offspring, adults * k


res = fib_rabbits(n_r, k_r)[0]

print(res)


