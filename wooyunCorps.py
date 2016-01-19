#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import time
import urllib
import urllib2
from bs4 import BeautifulSoup

def getPage(pageNum):
	try:
		url = 'http://www.wooyun.org/corps/page/' + str(pageNum)
		user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36'
		headers = {'user_agent' : user_agent}
		request = urllib2.Request(url , headers = headers)
		respond = urllib2.urlopen(request)
		content = respond.read().decode('utf-8')
		return content
	except urllib2.URLError, e:
		if hasattr(e , "code"):
			print e.code
		if hasattr(e , "reason"):
			print e.reason
	
def getItems(page):
	corpsPerPage = []
	soup = BeautifulSoup(page , "lxml")
	corps = soup.find_all(rel = "nofollow")
	for corp in corps:
		corpsPerPage.append(corp.string)
	return corpsPerPage
			
def getAll():
	pageNum = raw_input("Input the page numbers:")
	with file('/Users/MLS/Desktop/wooyunCorps.txt' , 'w+') as wooyun:
		for i in range(1 , int(pageNum)+1):
			page = getPage(i)
			print u"正在写入第" + str(i) + u"页厂商名字..."
			for j in getItems(page):
				wooyun.writelines(j + "\n")
			print u"写入完毕。"
			time.sleep(1)
		wooyun.close()

getAll()

