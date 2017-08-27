import json

import requests

client_id = '7a7ed764ce1792a88232'
client_secret = '0e3ffc02e46141784eb88685e2f4e25a'

# # инициируем запрос на получение токена
# r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
#                   data={
#                       "client_id": client_id,
#                       "client_secret": client_secret
#                   })
#
# # разбираем ответ сервера
# j = json.loads(r.text)
#
# # достаем токен
# token = j["token"]
# print(token)
token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJyb2xlcyI6IiIsImV4cCI6MTUwNDQyODgwNywiaWF0IjoxNTAzODI0MDA3LCJhdWQiOiI1OWEyODg4NzJhODkzYTJhMTk4ODEwNTUiLCJpc3MiOiJHcmF2aXR5IiwianRpIjoiNTlhMjg4ODcyYTg5M2EyOWY3ZTY5ZjgxIn0.82fRQfqqVmJV5HT5YiRVpMJE7oLESfe_vb86MYZkM6c'

# создаем заголовок, содержащий наш токен
headers = {"X-Xapp-Token": token}

url_base = "https://api.artsy.net/api/artists/{}"

results = dict()

with open("file4.txt") as rf:
    for data_id in rf.readlines():
        data_id = data_id.strip()
        # инициируем запрос с заголовком
        r = requests.get(url_base.format(data_id), headers=headers)

        # разбираем ответ сервера
        j = json.loads(r.text)
        birthday = int(j['birthday'])
        lst = results.get(birthday, [])
        lst.append(j['sortable_name'])
        results[birthday] = lst

print(results)
with open("result4.txt", "w", encoding='utf-8') as wf:
    for year in sorted(results.keys()):
        for e in sorted(results[year]):
            wf.write(e + "\n")
