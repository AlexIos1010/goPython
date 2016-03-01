#/usr/bin/python
# -*- coding: UTF-8 -*-

#Alex
 

#导入re模块
import re
  
# 将正则表达式编译成Pattern对象，注意hello前面的r的意思是“原生字符串”
pattern = re.compile(r'hello')
	 
# 使用re.search匹配文本，获得匹配结果，无法匹配时将返回None
result1 = re.search(pattern,'h hello hello h hellohellohellohellohelloello')
result2 = re.search(pattern,'helloo CQC!')
result3 = re.search(pattern,'helo CQC!')
result4 = re.search(pattern,'hello CQC!')
	  
#如果1匹配成功
if result1:
	# 使用search获得分组信息
	print result1
	print result1.group()
else:
	print '1匹配失败！'
									 
									  
#如果2匹配成功
if result2:
	# 使用search获得分组信息
	print result2.group()
else:
	print '2匹配失败！'
																	 
																	  
#如果3匹配成功
if result3:
	# 使用search获得分组信息
	print result3.group()
else:
	print '3匹配失败！'
																									 
#如果4匹配成功
if result4:
	# 使用search获得分组信息
	print result4.group()
else:
	print '4匹配失败！'
