# -*-coding:utf-8-*-
import sys
import os
import subprocess
logo=os.popen('cat evil.txt')
print logo.read()
print "~@^_^@~ evil0x python 工具合集~@^_^@~ "
print "说明:本程序除了自有代码，均不保证功能性，当然安全性各位可以自行查看"
print "为了方便扩展和减少代码量,及保证别人代码的完整性,采用了shell方式调用其他工具"
print  "1 evil0x自有工具                              2 扩展工具"
print  "3 kali系统过工具快捷调用              99 退出"
while True:
	select = raw_input("选择你要使用到功能：")
	if select  == '1':
		import tools1
	elif select =='2':
		import tools2
	elif select =='3':
		import tools3
	elif select =='99':
		sys.exit()
	else:
		print "输入有误，重新输入"
		continue
