import re

import requests

a = input().strip()
b = input().strip()

pattern = r'<a.*href=".*"'


results1 = re.findall(pattern, requests.get(a).text)
for r1 in [r.split('=')[1].strip('"') for r in results1]:
    results2 = re.findall(pattern, requests.get(r1).text)
    for r2 in [r.split('=')[1].strip('"') for r in results2]:
        if r2 == b:
            print('Yes')
            break
    else:
        continue
    break
else:
    print('No')
