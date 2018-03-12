# import pickle
# test_data = ['Save me!', 123.456, True]
# f = open('test.data', 'wb')
# pickle.dump(test_data, f)
#
# f.close()

# import pickle
#
# f = open("test.data","rb")
# test_data = pickle.load(f)
# f.close()
#
# print (test_data)


#coding:utf8
# 用一行 Python 代码实现：把1到100的整数里，能被2、3、5整除的数取出，以分号（;）分隔的形式输出。
print (';'.join([str(i) for i in range(1,101) if i%2==0 and i%3==0 and i%5==0])) #同时除尽
print (';'.join([str(i) for i in range(1,101) if i%2==0 or i%3==0 or i%5==0])) #单独
# print (';'.join(['1','1','1'])) #同时除尽
