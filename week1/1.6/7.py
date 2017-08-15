d = {}

n = int(input())
for i1 in range(n):
    s = input().split()
    cl = s[0]
    parents = []
    for j in range(2, len(s)):
        parents.append(s[j])
    d[cl] = parents


def find(p, c, results):
    if results.pop():
        results.append(True)
        return

    if p == c:
        results.append(True)
        return

    results.append(False)

    for e in d[c]:
        find(p, e, results)

results = []
n = int(input())
for i2 in range(n):
    p, c = input().split()
    results.append(False)
    find(p, c, results)

for r in results:
    if r:
        print('Yes')
    else:
        print('No')
