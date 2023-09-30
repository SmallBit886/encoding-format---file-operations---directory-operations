#
#file=open('b.txt','r') #以只读的模式打开文件
#file=open('b.txt','w') #以只写的形式打开文件
file=open('b.txt','a')  #以追加的形式打开文件
file1=open('a.txt','r+')#以读写的方式打开文件
file1.write('mamama')
print(file1.readlines())
file.write('python')
#print(file.readlines())    #只能写入
file.close()