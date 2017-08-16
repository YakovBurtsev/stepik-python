import os.path
import shutil

shutil.copy("test1.txt", "tests/test2.txt")

for current_dir, dirs, files in os.walk("."):  #from current dir
    print(current_dir, dirs, files)

shutil.copytree("tests", "tests/tests")
for current_dir, dirs, files in os.walk("."):  #from current dir
    print(current_dir, dirs, files)