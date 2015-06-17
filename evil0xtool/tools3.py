# -*-coding:utf-8-*-
import os
import sys
import subprocess
while True:
	print """欢迎使用kali 常用快捷调用
我们的目的是帮助大家快捷的打开一组程序甚至是帮忙设置参数
让普通人在不用预先学习软件的使用情况下获得自己想要的功能,
注意一定要使用kali系统,否则我们不保证能运行"""
	print "1 python   2 一键arp"
	print "3 wpscan       4 wireshark"
	select = raw_input("选择你要使用到功能：")
	if select  == '1':
		subprocess.Popen("python",shell=True)
	elif select =='2':
        #假设要打开多个程序,并且要依次成功才行
		n=subprocess.Popen("namp",shell=True)
		n.wait()
		p=subprocess.Popen("sqlmap",shell=True)
		p.wait()
		w=subprocess.Popen("wireshark",shell=True)
	elif select =='3':
		url=raw_input("请输入目标url:")
		cmd = 'wpscan '+ url
		print cmd
		subprocess.Popen(cmd,shell=True)
	elif select =='4':
		sys.exit()
