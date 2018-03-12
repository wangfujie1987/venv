#创建照片的存储目录 并按照照片的名词归档照片
import os
import exifread
import fnmatch
import shutil
dirsrc='F:\\testsrc'                   #照片目录
dirdst='F:\\testdst'                             #归档目录

#创建照片的存储目录
# for i in range(2003,2019):#年份
#     os.mkdir(dirdst+'\\'+str(i))
#     for j in range(1,13):#月份
#         dirname=str(i)+str(j)
#         os.mkdir(dirdst+'\\'+str(i)+'\\'+str(i)+'0'+str(j))
#         print(dirdst+'\\'+str(i)+'0'+str(j))

#归档照片
f = open(dirsrc+'\\'+'log.txt', "w") #打开日日志文件
i=0#记录成功的个数
j=0#记录失败的个数
for filename in os.listdir(dirsrc):  # 返回的filename为str类型
   try:
    #if os.path.splitext(filename)[1] =='.jpg' or os.path.splitext(filename)[1]=='.JPG':#是图片文件才进行处理
     shutil.move(dirsrc+'\\'+filename,dirdst+'\\'+filename[0:4]+'\\'+filename[0:6])
     #写入日志
     f.write(filename+' Moved successful\n')
     i+=1
   except:
     f.write(filename + ' Moved failed\n')
     j+=1
     continue
f.write('文件共%d个，成功归档%d个，失败%d个'%(i+j,i,j))
f.close()#关闭日志文件

