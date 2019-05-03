import os
import glob
import shutil

dir1 = 'Database/'

dir2 = 'next_ite/'


for names1 in os.listdir(dir1):
    if os.path.isdir(dir1 + names1):
        shutil.rmtree(dir1 + names1 + "/")

for names2 in os.listdir(dir2):
    if os.path.isdir(dir2 + names2):
        shutil.rmtree(dir2 + names2 + "/")

"""
files1 = glob.glob(dir1)
print(files1)
for f in files1:
    os.remove(f)

files2 = glob.glob(dir2)
print(files2)
for f in files2:
    os.remove(f)
"""