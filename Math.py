# a = "heaven"
# b = "hell"
# c = True and a or b
# print (c)
# d = False and a or b
# print (d)

import math

def get_pos(n):
    return (n/2, n*2)

x, y = get_pos(50)
print (x)
print (y)


def get_gen(a,b,c):
    math.sqrt(b*b-4*a*c)
    return (-b/2*a+(math.sqrt(b*b-4*a*c))/2*a,-b/2*a-(math.sqrt(b*b-4*a*c))/2*a)



print(get_gen(1,0,-64))