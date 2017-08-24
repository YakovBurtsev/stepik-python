import re

import requests

html_link = input().strip()


def f(links, strip_char, results):
    for link in [x.split('=')[1].strip(strip_char) for x in links]:
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
links1 = re.findall(r"<a.*href='.*'", text, flags=re.IGNORECASE)
links2 = re.findall(r'<a.*href=".*"', text, flags=re.IGNORECASE)
f(links1, "'", results)
f(links2, '"', results)


for r in results:
    print(r)