import sys, re

pattern = r'.*cat.*cat.*'

for line in sys.stdin:
    if re.match(pattern, line):
        print(line.rstrip())
