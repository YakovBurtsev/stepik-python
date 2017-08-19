s = input()
a = input()
b = input()

n = 0
if a not in s:
    print(0)
elif a in b:
    print("Impossible")
else:
    while True:
        s_last = s
        s = s.replace(a, b)
        if s_last == s and a not in s:
            print(n)
            break
        n += 1
