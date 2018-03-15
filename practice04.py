#!/usr/bin/env python
#
# import os
# import fnmatch
#
# for filename in os.listdir('.'):
#     if fnmatch.fnmatch(filename, '*.txt'):  # 匹配模式为星号，表示任意的字符
#         print(filename)
#
# print(os.listdir('.'))
#找出指定文件夹中的所有以txt结尾的文件，包括所有嵌套的子文件夹。

import os
import pygame
import fnmatch
import exifread

txtlist = []

for parent, dirnames, filename in os.walk("F:\\testdst"):

   # print(filename)

    for filenames in filename:
        txtlist.append(filenames)

print(fnmatch.filter(txtlist, '*.JPG')) #
print(len(fnmatch.filter(txtlist, '*.jpg'))) #
print(len(fnmatch.filter(txtlist, '*.mp4'))) #

