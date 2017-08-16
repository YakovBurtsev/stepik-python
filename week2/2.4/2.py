f = open("test1.txt", "w")
lst = ['line1', 'line2', 'line3']
s = '\n'.join(lst)
f.write(s)