with open("test.txt") as f, open("test_copy.txt", "w") as w:
    reversed_lines = reversed([line.rstrip() for line in f])
    w.write('\n'.join(reversed_lines))
