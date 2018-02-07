#-*- coding:utf-8 -*-

from email.Header import Header
from smtplib import SMTP_SSL
from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart
from email.utils import formataddr
import smtplib, time


def send_mail_attach(filename,current_time):
	mail_host="smtp.qq.com"  # 设置服务器
	mail_user="302416046@qq.com"    # 用户名
	mail_pass="nlpiqnuwfxyibhac"   # 口令
	#mail_host="mail.chinacreator.com"
	#mail_user="jiangshui.li@chinacreator.com"
	#mail_pass="109079"
	msg = MIMEMultipart()
	#att = MIMEText(open('report.html', 'rb').read(), 'base64', 'utf-8')
	att = MIMEText(open(filename, 'rb').read(), 'base64', 'utf-8')
	att["Content-Type"] = 'application/octet-stream'
	att["Content-Disposition"] = 'attachment; filename="report.html"'
	msg.attach(att)
	
	#msg['From'] = '302416046@qq.com'
	msg['From'] = formataddr(["李江水", "302416046@qq.com"])
	#msg['From'] = "jiangshui.li@chinacreator.com"
	
	receivers = """
		guiqiang.bian@chinacreator.com,
		shaobin.he@chinacreator.com
	"""
	ccs = """
		jiangshui.li@chinacreator.com,
		302416046@qq.com
		
	"""

	msg['To'] = receivers 	# 主送
	
	msg['CC'] = ccs			# 抄送
	
	#msg['subject'] = Header("中南e行测试结果(" +time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time()))+')','utf-8')
	msg['subject'] = Header("中南e行测试结果(" + current_time +')','utf-8')
	
	body = """<html>您好:<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;中南e行测试结果请见附件</html>"""
	#msg.attach(MIMEText(body, 'plain','utf-8'))
	msg.attach(MIMEText(body, 'html', 'utf-8'))
	
	#server = smtplib.SMTP(mail_host,25)
	server = smtplib.SMTP_SSL(mail_host)
	server.ehlo(mail_host)
	server.login(mail_user,mail_pass)
	msg_text=msg.as_string()
	
	
	server.sendmail(msg['From'],msg['To'].split(',')+msg['CC'].split(',') ,msg_text)
	server.quit()

if __name__=="__main__":
	current_time = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time()))
	send_mail_attach("F:/ljs/SouthChina/southchina/test_result/report.html",current_time)
