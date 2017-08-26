import sys, re

pattern = r'^(1(01*0)*1|0)*$'

for line in sys.stdin:
    line = line.rstrip()
    if re.match(pattern, line):
        print(line)


