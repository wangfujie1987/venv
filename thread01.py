# import urllib.request, time
#
# time_start = time.time()
# data = []
# for i in range(30):
#     # print ('request movie:', i)
#     id = 1764802 + i
#     url = 'https://api.douban.com/v2/movie/subject/%d' % id
#     d = urllib.request.urlopen(url).read()
#     data.append(d)
#     # print(type(data))
#     print ( i, time.time() - time_start)
#
# print ('data:', len(data))
#

# import urllib.request, time
# import json
#
# time_start = time.time()
# data = []
# # print ('request movie:', i)
# id = 1764802
# url = 'https://api.douban.com/v2/movie/subject/%d' % id
# d = urllib.request.urlopen(url).read()
# # data.append(d)
# # print(type(data))
# # print(i, time.time() - time_start)
# result=json.loads(d)#将json转化成字典
# print(d )
#

import urllib.request, time, threading


def get_content(i):
    id = 1764796 + i

    url = 'https://api.douban.com/v2/movie/subject/%d' % id

    d = urllib.request.urlopen(url).read()

    data.append(d)

    print( i, time.time() - time_start)

    print( 'data:', len(data))



time_start = time.time()
data = []
for i in range(30):
    print( 'request movie:', i)
    threading.start_new_thread(get_content, (i,))

raw_input('press ENTER to exit...\n')
