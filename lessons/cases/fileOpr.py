#/usr/bin/python
# -*- coding: UTF-8 -*-

#Alex



#传入图片地址，文件名，保存单张图片
def saveImg(self,imageURL,fileName):
	u = urllib.urlopen(imageURL)
	data = u.read()
	f = open(fileName, 'wb')
	f.write(data)
	f.close()



def saveText(self,content,name):
	fileName = name + "/" + name + ".txt"
  f = open(fileName,"w+")
  print "Saving Text",fileName
  f.write(content.encode('utf-8'))




#创建新目录
def mknewdir(self,path):
	path = path.strip()
  # 判断路径是否存在
  # 存在     True
  # 不存在   False
	isExists=os.path.exists(path)
    # 判断结果
	if not isExists:
	# 如果不存在则创建目录
 	# 创建目录操作函数
 		os.makedirs(path)
   	return True
	else:
	# 如果目录存在则不创建，并提示目录已存在
 		return False
