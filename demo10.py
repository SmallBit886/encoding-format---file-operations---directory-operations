#

file=open('d.txt','a')
file.write('hello')
file.close()    #文件关闭
file.write('world')
file.flush()    ##文件缓冲区

