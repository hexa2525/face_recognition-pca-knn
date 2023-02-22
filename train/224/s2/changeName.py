import os

files = os.listdir()
files.sort()
for i,file in enumerate(files):
    if(file != 'changeName.py'):
        os.system(f"mv {file} {i}.jpg")


