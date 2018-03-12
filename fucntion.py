def printAll(**kargs):
    for k in kargs:
        print( k ,':',kargs[k])



printAll(a=1, b=2, c=3)
printAll(x=4, y=5)