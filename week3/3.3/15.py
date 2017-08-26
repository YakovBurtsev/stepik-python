import sys, re

pattern = r'(\w)\1+'

for line in sys.stdin:
    line = line.rstrip()
    print(re.sub(pattern, r'\1', line))
