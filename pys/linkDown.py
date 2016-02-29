#-*-coding:utf-8-*-
import urllib
from sgmllib import SGMLParser

import os

class LinkParser(SGMLParser):
	linkList = []
	def reset(self):
		SGMLParser.reset(self)  #初始化
		self.linkList = []

	def start_a(self, attrs):
#		print "attrs:%s"%attrs
		linkUrl = [v for k, v in attrs if k==keylink]
#		print "linkUrl:%s\n\n"%linkUrl
		if linkUrl:
			self.linkList.append(linkUrl[0])
			linkUrl = ""

#pic source web   
url = raw_input("\nSource web:")
page = urllib.urlopen(url)
parser = LinkParser()
#pic dictionary key
keylink = "href"			#raw_input("Chose Download Elem:") 	
parser.feed(page.read())
#print parser.linkList
listlen = len(parser.linkList)
print "共有%d条链接"%listlen

link = raw_input("Add File Name:")
fullList = parser.linkList
str_list = '\n'.join(fullList)
linkDir = "./download/link"
flag = os.path.exists(linkDir)
if (flag!=True):
	os.mkdir(linkDir)
f = open("%s/%s.txt"%(linkDir,link),'wb')
f.write(str_list)
f.close()
print "Saved"
