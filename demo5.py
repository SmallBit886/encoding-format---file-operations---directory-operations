#以二进制方式进行读写操作
src_file=open('logo.png','rb')
target_file=open('copylogo.png','wb')

target_file.write(src_file.read())  #先读再写入

target_file.close()
src_file.close()