import sys, re

pattern = r'\ba+\b'

for line in sys.stdin:
    line = line.rstrip()
    print(re.sub(pattern, 'argh', line, count=1, flags=re.IGNORECASE))
