import json

data = json.loads(input())

d = dict()
for e in data:
    d[e["name"]] = e["parents"]


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


results = dict()
for p in d:
    res = []
    for c in d:
        res.append(False)
        find(p, c, res)
    results[p] = len([x for x in res if x])


for k in sorted(results.keys()):
    print(k, ":", results[k])