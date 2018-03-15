#测试 遍历目录下所有照片文件
import os
import exifread
import fnmatch
import shutil
import time
import datetime
# txtlist=[]
# def get_FileCreate_Time(filename):#filename包括为包括绝对名录的文件名
#    try:
#         timestamp=os.path.getctime(filename)#timestamp
#         date_time=datetime.datetime.fromtimestamp(timestamp)#格式化
#         return date_time
#    except:
#         return ('文件名错误')
# dir='F:\\test'
# dir1=dir+'\\'
# FIELD = 'EXIF DateTimeOriginal'
# for filename in os.listdir(dir):  # 返回的filename为str类型
#     fd = open(dir1 + filename, 'rb')
#     tags = exifread.process_file(fd)
#     fd.close()
#     print(tags)
#     if tags[FIELD]=='':
#         print('kong')
#     #print(tags[FIELD])
#

