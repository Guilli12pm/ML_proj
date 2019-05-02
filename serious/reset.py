import os
import glob

dir1 = 'pic/'
dir2 = 'next_ite/'


for filename1 in os.listdir(dir1):
    if filename1.endswith(".png"):
        os.remove(dir1 + filename1)

for filename2 in os.listdir(dir2):
    if filename2.endswith(".png"):
        os.remove(dir2 + filename2)

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