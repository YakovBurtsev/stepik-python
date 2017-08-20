import sys, re

pattern = r'\b(\w+)\1\b'

for line in sys.stdin:
    if re.match(pattern, line):
        print(line.rstrip())
