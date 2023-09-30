#文件的读写原理
file=open('a.txt','r')
print(file.readlines()) #放在一个列表当中
file.close()