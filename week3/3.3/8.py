import sys, re

pattern = r'.*\bcat\b.*'

for line in sys.stdin:
    if re.match(pattern, line):
        print(line.rstrip())