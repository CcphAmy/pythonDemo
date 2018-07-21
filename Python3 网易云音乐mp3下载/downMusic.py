import urllib.request
import requests
import os

from bs4 import BeautifulSoup

class HttpSvc():
	"""docstring for HttpSvc"""

	def __init__(self):
		super(HttpSvc, self).__init__()
		if not os.path.exists("d:/music"):
			os.mkdir('d:/music')
		
	def get(self,values):

		print(len(values))

		downNum    = 0

		for x in values:

			print('***** ' + x['name'] + '.mp3 ***** Downloading...')
			url = 'http://music.163.com/song/media/outer/url?id=' + x['id'] + '.mp3'
			try:
				urllib.request.urlretrieve(url,'d:/music/' + x['name'] + '.mp3')
				downNum = downNum + 1
			except:
				x = x - 1
				print('Download wrong~')

		print('Download complete ' + str(downNum) + 'files !')
		pass

	def getMusicData(self,id):

		user_agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36'
		headers    = {'User-Agent':user_agent}
		webData    = requests.get('https://music.163.com/playlist?id=' + id,headers=headers).text
		soup       = BeautifulSoup(webData,'lxml')

		find_list  = soup.find('ul',class_="f-hide").find_all('a')
		tempArr = []
		for a in find_list:
			music_id  = a['href'].replace('/song?id=','')
			music_name = a.text
			tempArr.append({'id':music_id,'name':music_name})
		return tempArr

if __name__ == '__main__':

	newHttp = HttpSvc()
	musicData = newHttp.getMusicData('2074950566') #获取歌单歌曲id
	print(newHttp.get(musicData))