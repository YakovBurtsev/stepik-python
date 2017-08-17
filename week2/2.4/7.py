import os

results = []
root_path = "C:\\Users\\yakov\\Desktop\\main"
for dirpath, dirsnames, filenames in os.walk(root_path):
    for file in filenames:
        if file.endswith(".py"):
            results.append(dirpath.replace(root_path, 'main'))
            break

results.sort()

with open("result.txt", "w") as w:
    w.write('\n'.join(results))