'''take picture, select the best and make a tar with all users'''

from os import system

system("python create_data.py")    #if doesn't work change python - python3
system("python check_photos.py")
system("python make_tar.py")
