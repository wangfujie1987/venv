f=open("scores.txt")
lines=f.readlines()#把文件数据读取成list 每一行是一个list元素
print(lines)
result=[]#定义结果的list
for line in lines:#循环中，每个循环为单行的字符串
    data=line.split()#再将字符串转化为list，文件中单行的字符串被空格分隔成list
    print(data)
    sum=0
    for i in data[1:]:#每个list内部做循环，将第2到最后一个元素相加
        sum+=int(i)
   # print(data[0])
   #  print(sum)
   #  print(data)
    result.append(data[0]+'\t'+':'+str(sum)+'\n')# 将单行的字符串append成为list
    results=''.join(result)#通过join将list合并成字符串
print(result)

f1=open("result.txt","w")
f1.write(results)
f1.close()
f.close()
# f1.close()
# f.close()
#print(data1)
#
# data=[1,23,4,4]
# for i in data:
#     print(i)
#
#
# data='hell word'
# #f=data.split()
# for f in data:
#  print(f)
#
# x=['安琪拉', '45', '89', '12', '12']
# print(x[0])

x=['sd','sdf']
y=['sd1','sdf1']
print(x+y)