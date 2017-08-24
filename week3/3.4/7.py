import re

import requests

html_link = input().strip()


def f(links, pattern, strip_char, results):
    for lst in [re.findall(pattern, x, flags=re.IGNORECASE) for x in links]:
        for link in lst:
            # print(link)
            link = link.strip(strip_char)
            if link.startswith(".."):
                continue
            if "://" in link:
                link = link.split("://")[1]
            if "/" in link:
                link = link.split("/")[0]
            if ":" in link:
                link = link.split(":")[0]
            results.add(link)


text = requests.get(html_link).text

results = set()
links1 = re.findall(r"<a.*?href='.+?'>", text, flags=re.IGNORECASE)
links2 = re.findall(r'<a.*?href=".+?">', text, flags=re.IGNORECASE)
# print(links1)
# print(links2)
f(links1, r"href='.+?'", "'", results)
f(links2, r'href=".+?"', '"', results)

for r in sorted(results):
    print(r)