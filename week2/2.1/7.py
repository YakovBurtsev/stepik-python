d = {}

n = int(input())
for i1 in range(n):
    s = input().split()
    d[s[0]] = s[2::]

m = int(input())
in_list = []
for i2 in range(m):
    in_list.append(input())

lst = []
results = []


def find(p, c):
    if lst.pop():
        lst.append(True)
        return

    if p == c:
        lst.append(True)
        return

    lst.append(False)

    for e in d[c]:
        find(p, e)

in_list.reverse()
for i, cl in enumerate(in_list):
    for p in in_list[i+1:]:
        lst.append(False)
        find(p, cl)
        if lst.pop():
            if cl not in results:
                results.append(cl)

for r in reversed(results):
    print(r)
