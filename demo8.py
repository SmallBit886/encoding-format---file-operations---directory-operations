#文件对象的常用方法
file=open('c.txt','r')
#hellojavagopython
file.seek(2)    #跳过两个字节 #将文件指针移动到新的位置
print(file.read())  #llojavagopython
print(file.tell())  #17 #返回文件指针的当前位置    #位置从0开始算的

file.close()