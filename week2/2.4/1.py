# r - read (default)
# w - write
# a - append

f = open("test.txt", "r")

# print(f.read(5))
# print(f.read())

# x = f.read()
# x = x.splitlines()
# print(repr(x))

# x = f.readline()
# print(x)

for line in f:
    line = line.rstrip()
    print(repr(line))

