
# 从1~n中，随机取m个数。1<=m<=n  第一种算法
# from random import randint
#
# result=[]
# print('----------请输入最大数字-------------')
#
# n=int(input())
#
# print('----------请输入数字个数------------')
#
# m=int(input())
#
# # for i in range(0,m):
# #     num=randint(1,n)
# #     result.append(num)
# i=0
#
# def isduplicate():
#     global  num
#     for j in range(0, len(result)):
#         if  num == result[j]:
#             num = randint(1, n)
#             # 取到重复的值，重新取值并且继续循环
#             isduplicate()
#         else:
#             continue  # 没有取到重复值
# while 1 :
#    # i+=1
#    num=randint(1,n)
#    # for j in range(0,len(result)):
#    #     if num==result[j]:
#    #         num=randint(1,n)
#    #         isduplicate() #取到重复的值，重新取值并且继续循环
#    #     else:
#    #         continue #没有取到重复值
#    isduplicate()
#    result.append(num)
#    if len(result)>=m:
#        break
#
#
# print(result)

#另外一种写法

# 从1~n中，随机取m个数。1<=m<=n
# from random import randint
# #
# # num=randint(1,10)
# #
# # print(num)
# result=[]
# print('----------请输入最大数字-------------')
#
# n=int(input())
#
# print('----------请输入数字个数------------')
#
# m=int(input())
#
# # for i in range(0,m):
# #     num=randint(1,n)
# #     result.append(num)
# i=0
# def isduplicate():
#     global  num
#     for j in range(0, len(result)):
#         if  num == result[j]:
#             # num = randint(1, n)
#             return True
#         else:
#             continue  # 没有取到重复值
#     return False
# while 1 :
#    # i+=1
#    num=randint(1,n)
#    duplicate = True
#    while duplicate:
#        num = randint(1, n)
#        duplicate=isduplicate()
#
#    result.append(num)
#    if len(result)>=m:
#        break
#
#
# print(result)
#
# 最简单写法：
import random
result=[]
print('----------请输入最大数字-------------')
n=int(input())
print('----------请输入数字个数------------')
m=int(input())
result=random.sample(range(1,n),m)
print(result)

