import requests
import os

from bs4 import BeautifulSoup



class GanJi():
    """docstring for GanJi"""

    def __init__(self):
        super(GanJi, self).__init__()

    def get(self,url):

        user_agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36'
        headers    = {'User-Agent':user_agent}
        
        webData    = requests.get(url + 'o1',headers=headers).text
        soup       = BeautifulSoup(webData,'lxml')
        
        
        sum        = soup.find('span',class_="num").text.replace("套","")
        ave        = int(sum) / 32
        forNum     = int(ave)

        if forNum < ave:
            forNum = forNum + 1


        for x in range(forNum):
            webData    = requests.get(url + 'o' + str(x + 1),headers=headers).text
            soup       = BeautifulSoup(webData,'lxml')
            find_list  = soup.find('div',class_="f-main-list").find_all('div',class_="f-list-item ershoufang-list")

            for dl in find_list:
                
                print(dl.find('a',class_="js-title value title-font").text,end='|') # 名称

                # 中间 5 个信息
                tempDD = dl.find('dd',class_="dd-item size").find_all('span')
                for tempSpan in tempDD:
                    if not tempSpan.text == '' : 
                        print(tempSpan.text.replace("\n", ""),end='|')

                
                print(dl.find('span',class_="area").text.replace(" ","").replace("\n",""),end='|') # 地址
                
                print(dl.find('div',class_="price").text.replace(" ","").replace("\n",""),end='|') # 价钱
                
                print(dl.find('div',class_="time").text.replace(" ","").replace("\n",""),end="|") # 平均
                
                print("http://chaozhou.ganji.com" + dl['href'],end="|") # 地址

                print(str(x + 1))

if __name__ == '__main__':
    temp = GanJi()
    temp.get("http://chaozhou.ganji.com/fang5/xiangqiao/")