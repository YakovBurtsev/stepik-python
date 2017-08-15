d = {}


def create(parent, name):
    d[name] = {'parent': parent, 'vars': set()}


def add(name, var):
    d[name]['vars'].add(var)


def get(name, var):
    if var in d[name]['vars']:
        return name
    parent = d[name]['parent']
    if parent:
        return get(parent, var)
    return None


n = int(input())
results = []
create(None, 'global')
for i in range(n):
    command, name, var = input().split()
    if command == 'add':
        add(name, var)
    elif command == 'create':
        create(parent=var, name=name)
    elif command == 'get':
        results.append(get(name, var))

for e in results:
    print(e)
