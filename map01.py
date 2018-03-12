lst_1 = [1,2,3,4,5,6]
lst_2 = [1,3,5,7,9,11]
lst_3 = list(map(None, lst_1))
print (lst_3)
lst_4 = list(map(None, lst_1, lst_2))
print (lst_4)
#
# lst_1 = [1,2,3,4,5,6]
# def double_func(x):
#  return x * 2
# lst_2 = list(map(double_func, lst_1))
# print (lst_2)
