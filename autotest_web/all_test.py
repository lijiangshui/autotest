#-*- coding:utf:8 -*-

import sys
sys.path.append("./test_case/package")
sys.path.append("./test_case")
#from sendmail import send_mail_attach
from sendmail1 import send_mail_attach
import unittest,doctest
import time
import HTMLTestRunner


def all_case_list():
	all_testcase_names = [
	"test_login",
	"test_personinfo"
	]
	
	return all_testcase_names
	

if __name__ == "__main__":
	
	suite = doctest.DocTestSuite()
	for test_case_name in all_case_list():
		print test_case_name
		suite.addTest(unittest.defaultTestLoader.loadTestsFromName(test_case_name))
	
	current_time= time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time()))
    
	filename= "./report/"+ current_time +"_report.html"
	fp = file(filename,"wb")
    
	runner=HTMLTestRunner.HTMLTestRunner(
		stream=fp,
		title=u"中南e行信息门户",
		description=u"中南e行信息门户测试"
	)
	runner.run(suite)
	fp.close()
	time.sleep(1)
	#send_mail_attach(filename,current_time)

