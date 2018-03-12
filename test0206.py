
# 从1~n中，随机取m个数。1<=m<=n
from random import randint
#
# num=randint(1,10)
#
# print(num)
result=[]
print('----------请输入最大数字-------------')

n=int(input())

print('----------请输入数字个数------------')

m=int(input())

# for i in range(0,m):
#     num=randint(1,n)
#     result.append(num)
i=0
def isduplicate():
    global  num
    for j in range(0, len(result)):
        if  num == result[j]:
            # num = randint(1, n)
            return True
        else:
            continue  # 没有取到重复值
    return False
while 1 :
   # i+=1
   num=randint(1,n)
   duplicate = True
   while duplicate:
       num = randint(1, n)
       duplicate=isduplicate()

   result.append(num)
   if len(result)>=m:
       break


print(result)

