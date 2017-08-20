import sys, re

pattern = r'.*z.{3}z.*'

for line in sys.stdin:
    if re.match(pattern, line):
        print(line.rstrip())