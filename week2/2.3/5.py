import itertools


def primes():
    x = 1
    while True:
        x += 1
        k = 0
        for i in range(2, x):
            if x % i == 0:
                k += 1
        if k == 0:
            yield x


print(list(itertools.takewhile(lambda x : x <= 31, primes())))