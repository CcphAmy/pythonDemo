import requests
import json
import smtplib
import sys
import time
from random import randint
from email.mime.text import MIMEText
from email.header import Header
class tl12306:
    def __init__(self):
        self.num = 1
        # 替换为你要查询的url地址
        self.url = 'https://kyfw.12306.cn/otn/leftTicket/queryA?leftTicketDTO.train_date=2018-09-30&leftTicketDTO.from_station=IZQ&leftTicketDTO.to_station=CBQ&purpose_codes=ADULT'
    def getlist(self):
        try:
            r = requests.get(self.url)
            if r.status_code == 200:
                j    = json.loads(r.text)
                k    = j['data']
                str1 = ""

                strData = ["G6305","D7501","G6325","D7521","D7533","D7529","D2381","G6337","D7525","G6321","D7513","G6313","G1607","G6309","D7533","D7517","G6329","D7505","G6345","G6341"]

                for r in k['result']:
                    for cs in strData:
                        if "|" + cs+"|" in r:
                            if r.split('|')[-7] != '无': #二等座
                                str1 = str1 + cs + ',有票啦~~\n'
                if len(str1)>5:
                    print(str1)
                    self.send_mail(str1)


                sys.stdout.write('\r')
                sys.stdout.write('已查询%d次~' % self.num)
                sys.stdout.flush()
                self.num+=1
            else:
                msg = '获取车票信息失败~~'
                print(msg)
                self.send_mail(msg)
        except Exception as e:
            print(e)
    def send_mail(self,str):
        # 第三方 SMTP 服务
        mail_host = "smtp.qq.com"  # 设置服务器
        mail_user = "********@qq.com"  # 用户名 发送者的邮箱
        mail_pass = "****************"  # 口令 登录邮箱开启POP3/SMTP服务，输入授权码
        sender = '********@qq.com' #  发送者的邮箱
        receivers = ['********@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
        message = MIMEText(str, 'plain', 'utf-8')
        message['From'] = Header("肥肥", 'utf-8') 
        message['To'] = Header("圆圆", 'utf-8')
        message['Subject'] = Header("余票提醒", 'utf-8')
        try:
            smtpObj = smtplib.SMTP()
            smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
            smtpObj.login(mail_user, mail_pass)
            smtpObj.sendmail(sender, receivers, message.as_string())
            print("邮件发送成功")
        except smtplib.SMTPException:
            print("Error: 无法发送邮件")

if __name__ == '__main__':
    c = tl12306()
    print('监控中~')
    while True:
        c.getlist()
        time.sleep(randint(5,10))