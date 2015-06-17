# -*-coding:utf-8-*-
import sys
import subprocess
import os
print """ *****************************************************
欢迎使用evil0x扩展工具合集,工具创意均来自网上公开源码工具,本着代码开源原则
evil0x不会对其做任何更改，各位使用全凭自愿 
******************************************************        """
while True:
	print "1 wifi钓鱼        2 test.py "
	print "3 test       99 退出"
	select = raw_input("选择你要使用到功能：")
	if select  == '1':
		os.Popen("python tools2/HH_wifiphisher/H_wifiphisher.py")
		continue
	elif select =='2':
		import tools2\test1
		continue
	elif select =='3':
		print " test 3"
	elif select =='99':
		sys.exit()
	else:
		print "输入的选项有错误,重新选择"
		continue
		
	
