import os
import shutil
os.chdir('C:\\')

dir_src = ("C:\Users\Student\Desktop\A\\")
dir_dst = ("C:\Users\Student\Desktop\B\\")

'''
for filename in os.listdir(dir_src):
    if filename.endswith('.txt'):
        shutil.move(dir_src + filename, dir_dst)
    print(filename)
    print(dir_dst)
'''

#Consolidating the code into a function.
def moveFunc(source, destination):
    for filename in os.listdir(dir_src):
        if filename.endswith('.txt'):
            shutil.move(dir_src + filename, dir_dst)
        print(filename)
        print(dir_dst)
moveFunc(dir_src, dir_dst)
