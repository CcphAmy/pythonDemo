import urllib
import urllib.parse
import urllib.request

import os

class HttpSvc():
	"""docstring for HttpSvc"""

	def __init__(self):
		super(HttpSvc, self).__init__()
		if not os.path.exists("d:/music"):
			os.mkdir('d:/music')
		
	def get(self,values):

		print(len(values))

		user_agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36'
		headers    = {'User-Agent':user_agent}
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

	def write(self,fileName):
		pass

print("下载歌单所有歌曲")

# 已爬歌单

getMusicData = [
	{'id':'440208476','name':'That Girl-Olly Murs'},
	{'id':'29966565','name':'Love Me Like You Do（电影《五十度灰》主题曲）-Ellie Goulding'},
	{'id':'32019002','name':'Beautiful Now-Zedd Jon Bellion'},
	{'id':'812400','name':'PLANET-ラムジ'},
	{'id':'524290990','name':'What Lovers Do-Maroon 5 SZA'},
	{'id':'809268','name':'sweets parade-花澤香菜'},
	{'id':'525278524','name':'无问（电影《无问西东》宣传曲）-毛不易'},
	{'id':'526464293','name':'空空如也-任然'},
	{'id':'32192436','name':'绅士-薛之谦'},
	{'id':'287617','name':'逃亡-孙燕姿'},
	{'id':'387717','name':'海阔天空-信乐团'},
	{'id':'27867449','name':'倾城-陈奕迅'},
	{'id':'298489','name':'座右铭-吴雨霏'},
	{'id':'31654343','name':'不将就（电影《何以笙箫默》片尾主题曲）-李荣浩'},
	{'id':'287749','name':'天黑黑-孙燕姿'},
	{'id':'191528','name':'够钟-周柏豪'},
	{'id':'25788001','name':'其实都没有-杨宗纬'},
	{'id':'28314060','name':'听海-张惠妹'},
	{'id':'287063','name':'我怀念的-孙燕姿'},
	{'id':'190270','name':'饿狼传说-张学友'},
	{'id':'529747143','name':'贪图-蔡健雅'},
	{'id':'31445554','name':'七月上-Jam'},
	{'id':'65766','name':'富士山下-陈奕迅'},
	{'id':'110452','name':'爱转角（电视剧《转角遇到爱》片尾曲）-罗志祥'},
	{'id':'65198','name':'命硬-侧田'},
	{'id':'256468','name':'至少还有你-林忆莲'},
	{'id':'453062799','name':'你知道我在等你吗（Cover 白百合）-刘半仙'},
	{'id':'354593','name':'我们的爱-F.I.R.'},
	{'id':'29414037','name':'走马-陈粒'},
	{'id':'287248','name':'第一天-孙燕姿'},
	{'id':'176999','name':'情非得已（电视剧《流星花园》主题曲）-庾澄庆'},
	{'id':'307109','name':'我要的世界-萧亚轩'},
	{'id':'30431375','name':'历历万乡-陈粒'},
	{'id':'286980','name':'雨天-孙燕姿'},
	{'id':'29713754','name':'匆匆那年（Fleet of Time）-王菲'},
	{'id':'108914','name':'江南-林俊杰'},
	{'id':'191232','name':'遥远的她-张学友'},
	{'id':'280120','name':'梦一场（电视剧《新闻小姐》插曲）-那英'},
	{'id':'525112245','name':'This Is Me (From The Greatest Showman)-Kesha'},
	{'id':'4259981','name':'Sorry-Queensberry'},
	{'id':'32341765','name':'Smile-Dami Im'},
	{'id':'25657282','name':'Marry You-Bruno Mars'},
	{'id':'5253801','name':'Free Loop-Daniel Powter'},
	{'id':'16431842','name':'Innocence-Avril Lavigne'},
	{'id':'21038756','name':'Just Dance-Lady Gaga RedOne Colby O Donis'},
	{'id':'485960228','name':'岁月神偷（电影《逆时营救》主题曲）-周笔畅'},
	{'id':'523251118','name':'说散就散（电影《前任3：再见前任》主题曲）-袁娅维'}
]

newHttp = HttpSvc()

print(newHttp.get(getMusicData))