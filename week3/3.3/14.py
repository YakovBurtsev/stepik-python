import sys, re

pattern = r'\b(\w)(\w)(\w*)\b'

for line in sys.stdin:
    line = line.rstrip()
    print(re.sub(pattern, r'\2\1\3', line))
