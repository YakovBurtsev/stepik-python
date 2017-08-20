import sys, re

pattern = r'human'

for line in sys.stdin:
    line = line.rstrip()
    print(re.sub(pattern, 'computer', line))
