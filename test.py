i = 0
while True:
    if i == 0:
        break
    i += 1
else:
    print("this else in while")

for i in range(10):
    a = i * i
    if a > 10000:
        break
else:
    print("this else in for")
