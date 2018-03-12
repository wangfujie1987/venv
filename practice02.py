#将list中重复值去掉，插入到另外一个list中
num=[7,7,7,7,7,7,7,5,5,5,3,4,5,6,6,6,6,6,6,6,6,6,6,6,6,6,6,7,8,9,0,9,9,8,7,6,5,10000000]
numnew=[]
#算法一（思路是先去除重复，再冒泡法排序）
#去除重复函数
# def ifexist(number):
#     global numnew
#     for i in numnew:
#         if number==i:
#             return True#如果存在相同则终止循环，返回true
#         else:
#             continue#如果不一样，则继续在新list中作比较
#     return False#最后都不一样，返回False
# for i in num:
#     if not ifexist(i):
#      numnew.append(i)
# # numnew.sort()
# temp=0
# #冒泡法排序
# for i in range(0,len(numnew)):
#     for j in range(0,len(numnew)-1):
#         if numnew[j]>numnew[j+1]:
#             temp=numnew[j]
#             numnew[j]=numnew[j+1]
#             numnew[j+1]=temp
# print(numnew)
#

#写法二 直接调用list的sorted和set函数

numnew=sorted(set(num))


print(numnew)
print(set(num))
print(sorted(num))





# for i in num:
#    m=num.count(i)
#    if m>1:
#        num.remove(i)
# print(num)



