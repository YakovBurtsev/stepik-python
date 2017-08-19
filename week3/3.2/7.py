s = input()
t = input()

n = 0
for i in range(len(s)):
    if s[i:].find(t) == 0:
        n += 1

print(n)