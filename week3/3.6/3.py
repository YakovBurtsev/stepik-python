import requests

url = "http://numbersapi.com/{}/math?json=true&default=number+is+boring"
with open("filename.txt") as rf, open("result.txt", "w") as wf:
    for number in rf:
        url_format = url.format(number.strip())
        data = requests.get(url_format).json()
        if "number is boring" == data["text"]:
            wf.write("Boring\n")
        else:
            wf.write("Interesting\n")