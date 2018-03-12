# -*- coding: UTF-8 -*-
import urllib.request# 2.X对应的urllib2
from city import city
import json
result=''
#首先，抓取省份的列表：
url1 = 'http://m.weather.com.cn/data3/city.xml'
content1 = urllib.request.urlopen(url1).read().decode("utf-8")
provinces = content1.split(',')#，网站返回的数据是以逗号分隔的字符串，通过split转化成list
#print(provinces)

#对于每个省，抓取城市列表
url = 'http://m.weather.com.cn/data3/city%s.xml'
result = 'city = {\n'
for p in provinces[:33]:
    p_code = p.split('|')[0]
    url2 = url % p_code
    content2 = urllib.request.urlopen(url2).read().decode("utf-8")
    cities = content2.split(',')
    #print(cities)
    #再对于每个城市，抓取地区列表：
    for c in cities:
        c_code=c.split('|')[0]
        url3=url%c_code
        content3=urllib.request.urlopen(url3).read().decode("utf-8")
        districts=content3.split(',')
        #print(districts)
        #最后，对于每个地区，我们把它的名字记录下来，然后再发送一次请求，得到它的最终代码：
        for d in districts:
            d_pair = d.split('|')
            d_code = d_pair[0]
            name = d_pair[1]
            url4 = url % d_code
            content4 = urllib.request.urlopen(url4).read().decode("utf-8")
            code = content4.split('|')[1]
            line = "    '%s': '%s',\n" % (name, code)
            result += line
            print (name + ':' + code)
result += '}'
f=open('city01.py','w',encoding="utf-8")# 增加encoding参数解决写入中文乱码问题
f.write(result)
f.close()

