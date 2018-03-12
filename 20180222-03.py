# import re
# text = "Hi, I am Shirley Hilton. I am his wife."
# m = re.findall(r"I.*e", text)
# if m:
#     print (m)
# else:
#     print ('not match')
#
#
# print('\\be')

import random
num=random.random()
num=random.uniform(1,10000000000)

print(num)


str=random.choice([1, 2, 3, 5, 8, 13]) #list
str1=random.choice('hello') #字符串
str2=random.choice(['hello', 'world']) #字符串组成的list
str3=random.choice((1, 2, 3)) #元组

print(str)
print(str1)
print(str2)
print(str3)

a=[1, 2, 3, 5, 8, 13]
random.shuffle(a)
print(a)

random.seed(x)
