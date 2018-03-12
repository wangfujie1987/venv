def isCoordinate(x,y):
    if x>0:
        if y>0:
            return 1
        else:
            return 4
    else:
        if y>0:
            return 2
        else:
            return 3


print('Please input X')
x=int(input())
print('Please inmput Y')
y=int(input())

z=isCoordinate(x,y)
print(z)