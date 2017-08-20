import sys, re

pattern = r'.*\\.*'

for line in sys.stdin:
    if re.match(pattern, line):
        print(line.rstrip())