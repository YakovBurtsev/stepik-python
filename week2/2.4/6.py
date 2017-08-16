import os.path


print(os.listdir())
print(os.getcwd())
print(os.listdir("tests"))

print(os.path.exists("test.txt"))
print(os.path.exists("random.txt"))

print(os.path.isdir("test.txt"))
print(os.path.isfile("test.txt"))

print(os.path.abspath("test.txt"))

print(os.getcwd())
os.chdir("tests")
print(os.getcwd())


