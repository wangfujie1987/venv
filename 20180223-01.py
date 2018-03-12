# import re
# text = "site sea sue sweet see se case sse ssee loses"
# m = re.findall(r"\bs\S*?e\b", text)
# if m:
#     print (m)
# else:
#     print ('not match')
#
#
# print('\be\tf')
import time
starttime = time.time()
print ('start:%f' % starttime)
for i in range(10):
    print (i)
endtime = time.time()
print ('end:%f' % endtime)
print ('total time:%f' % (endtime-starttime) )

