f=open("scores.txt")
lines=f.readlines()#把文件数据读取成list 每一行是一个list元素
print(lines)
#result=['','','']#定义结果的list
results=[]
for line in lines:#循环中，每个循环为单行的字符串
    data=line.split()#再将字符串转化为list，文件中单行的字符串被空格分隔成list
    #print(data)
    sum=0
    for i in data[1:]:#每个list内部做循环，将第2到最后一个元素相加
        sum+=int(i)
   # print(data[0])
   #  print(sum)
   #  print(data)

   # result+=[data[0],':',str(sum)+'\n']#将结果赋值给list，并通过"+"操作合并所有list元素
    result='%s\t:%d\n'%(data[0],sum)#直接赋值给字符串
    print(result)
    results.append(result)#将字符串append形成list，
    print(results)
    #results=''.join(result)#通过join将list合并成字符串
#print(results)

f1=open("result1.txt","w")
f1.writelines(results)
# f1.close()
# f.close()
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
x=[]
for i in range(1,10):
    x.append(i)

print(x)
