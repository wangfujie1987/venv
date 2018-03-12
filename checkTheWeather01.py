# -*- coding: UTF-8 -*-
import urllib.request# 2.X对应的urllib2
from city01 import city
import json

content='s'
# cityname = input('你想查哪个城市的天气？退出请输入q\n')
# citycode = city.get(cityname)

while 1:
  try:
   cityname = input('你想查哪个城市的天气？退出请输入q\n')
   if cityname=='q':
       break
   citycode = city.get(cityname)
   url = 'http://www.weather.com.cn/data/cityinfo/%s.html' % citycode
   content = urllib.request.urlopen(url).read().decode("utf-8")
   #print(url)
   #print(content)
   data=json.loads(content)#将json转化成字典
   # print(data)
   # print(type(content))
   # print(type(data))
   result = data['weatherinfo']
   str_temp = ('%s\n%s ~ %s') % (
       result['weather'],
       result['temp1'],
       result['temp2']
   )
   print(str_temp)
  except:
      print('查询失败-找不到对应城市！')
      break
# else:
print("查询结束")

