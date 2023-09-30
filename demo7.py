#
file=open('c.txt','a')
#file.write('hello')    #将字符串内容写入文件中
lst=['java','go','python']
file.writelines(lst)    #将字符串列表追加到文件中
file.close()

