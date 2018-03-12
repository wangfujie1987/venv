# sum = 0
# for i in range(1, 101):
# 	sum += i
# print (sum)

from functools import reduce
lst = range(1, 101)
print(lst)
def add(x, y):
	return x + y
print (reduce(add, lst))
