import os.path

for current_dir, dirs, files in os.walk("."):  #from current dir
    print(current_dir, dirs, files)