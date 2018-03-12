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

import fnmatch
import exifread

txtlist = []

for parent, dirnames, filename in os.walk("F:\彤彤手机备份20180210"):

   # print(filename)


    for filenames in filename:
        txtlist.append(filenames)

print(fnmatch.filter(txtlist, '*.JPG')) #
