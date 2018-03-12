f = open('data1.txt')
f1= open('测试.doc','w')
data=f.read()
f1.write(data)
#data = f.readline()
#print (data)

f.close()
f1.close()

# print("Please input a sentence")
#
# data=input()
# #data='I am Dennis .\nI have a son named Damai'
# f=open('Damai.doc','w')
# f.write(data)
# f.close()