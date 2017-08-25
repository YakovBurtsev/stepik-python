import re

import requests

html_link = input()
# html_link = 'https://stepic.org/media/attachments/lesson/24471/03'
text = requests.get(html_link).text

results = set()
links = re.findall("""<a .*?href=['"](.+?)['"].*?>""", text, flags=re.IGNORECASE)
# print(links)
for link in links:
    if link.startswith(".."):
        continue
    if "://" in link:
        link = link.split("://")[1]
    if "/" in link:
        link = link.split("/")[0]
    if ":" in link:
        link = link.split(":")[0]
    results.add(link)


for r in sorted(results):
    print(r)
