import math


def cnk(n, k):
    if k == 0:
        return 1
    elif k > n:
        return 0
    else:
        return cnk(n - 1, k) + cnk(n - 1, k - 1)


def cnk_formula(n, k):
    return math.factorial(n) // (math.factorial(k) * math.factorial(n-k))


n, k = map(int, input().split())
print(cnk_formula(n, k))
print(cnk(n, k))
