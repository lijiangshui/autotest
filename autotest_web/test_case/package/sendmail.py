# -*- coding: UTF-8 -*-

from email.Header import Header
from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart
import smtplib, datetime


def send_mail_attach(filename):
	mail_host="mail.chinacreator.com"  # 设置服务器
	mail_user="jiangshui.li"    # 用户名
	mail_pass="109079"   # 口令 
	msg = MIMEMultipart()
	att = MIMEText(open(filename, 'rb').read(), 'base64', 'utf-8')
	att["Content-Type"] = 'application/octet-stream'
	att["Content-Disposition"] = 'attachment; filename="report.html"'
	msg.attach(att)
	
	msg['From'] = 'jiangshui.li@chinacreator.com'
	
	#receivers = """
	#	guiqiang.bian@chinacreator.com,
	#	302416046@qq.com,
	#	shaobin.he@chinacreator.com
	#"""
	receivers = """
		302416046@qq.com

	"""
	ccs = """
		jiangshui.li@chinacreator.com
	"""

	msg['To'] = receivers 	# 主送
	
	msg['CC'] = ccs			# 抄送
	
	msg['subject'] = Header('测试结果..... (' + str(datetime.date.today()) + ')','utf-8')
	
	body = "Python test mail"
	msg.attach(MIMEText(body, 'plain'))
	
	server = smtplib.SMTP(mail_host,25)
	server.login(mail_user,mail_pass)
	msg_text=msg.as_string()
	server.sendmail(msg['From'], msg['To'].split(',')+msg['CC'].split(','),msg_text)
	server.close

if __name__=="__main__":
	send_mail_attach("F:/ljs/SouthChina/southchina/test_result/report.html")
