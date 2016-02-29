#-*-coding:utf-8-*-
import urllib
from sgmllib import SGMLParser

import os

class PicParser(SGMLParser):
	imgList = []
	def reset(self):
		SGMLParser.reset(self)  #初始化
		self.imgList = []
	def start_img(self, attrs):
		keyTitle = "src"        #pic dictionary key
		imgUrl = [v for k, v in attrs if k==keyTitle]
		if imgUrl:
			self.imgList.append(imgUrl[0])
			imgUrl = ""

#pic source web   
url = raw_input("Pic source web:")
page = urllib.urlopen(url)
parser = PicParser()
parser.feed(page.read())
#print parser.imgList
listlen = len(parser.imgList)
print "共有图片%d张"%listlen

startS = raw_input("Start:");
start = int(startS)-1
endS = raw_input("End:");
end = int(endS)
cnt = start+1
iPre = raw_input("Add Pic Prefix:")
fullList = parser.imgList
downList = fullList[start:end]
for url in downList:
#	print url
	imgDir = "./download"
	flag = os.path.exists(imgDir)
	if (flag!=True):
		os.mkdir(imgDir)
	f = open("%s/%s%d.jpg"%(imgDir,iPre,cnt),'wb')
	img = urllib.urlopen(url)
	imgB = img.read()
	f.write(imgB)
	f.close()
	print "%s%d was done!"%(iPre,cnt)
	cnt += 1
