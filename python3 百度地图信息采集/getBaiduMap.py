import requests
import os
import json
from bs4 import BeautifulSoup

class BaiduMap(object):
	"""docstring for BaiduMap"""
	def __init__(self):
		super(BaiduMap, self).__init__()


	#城市获取数据
	def getCityData(cityName):
		# http://map.baidu.com/?newmap=1&qt=cur&ie=utf-8&wd=  &oue=1&res=jc
		try:
			webData = requests.get("http://map.baidu.com/?newmap=1&qt=cur&ie=utf-8&wd=" + cityName + "&oue=1&res=jc").text
			jsonData = json.loads(webData)
			# print(jsonData)

			if 'weather' in jsonData : #存在天气预报的情况下
				weatherData = json.loads(jsonData['weather'])
				print(weatherData['OriginQuery']," PM2.5:",weatherData['pm25'],weatherData['weather0'],"[",weatherData['temp0'],"][",weatherData['wind0'],"]")


		except Exception as e:
			raise


if __name__ == '__main__':
	BaiduMap.getCityData("广州");