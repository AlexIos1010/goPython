#/usr/bin/python
# -*- coding: UTF-8 -*-

#Alex

import re

pattern = re.compile(r'\d+')
print "\nre.finditer:",re.finditer(pattern,'one1two2three3four4')
for m in re.finditer(pattern,'one1two2three3four4'):
	print "\nm:",m
	print "m.group():",m.group(),

			### 输出 ###
"""

re.finditer: <callable-iterator object at 0x10ee532d0>

m: <_sre.SRE_Match object at 0x10ee4eac0>
m.group(): 1 
m: <_sre.SRE_Match object at 0x10ee4eb28>
m.group(): 2 
m: <_sre.SRE_Match object at 0x10ee4eac0>
m.group(): 3 
m: <_sre.SRE_Match object at 0x10ee4eb28>
m.group(): 4
"""
