#os模块操作目录相关函数
import os
print(os.getcwd())  #返回当前的工作目录  #G:\Python1\chap15

#返回指定路径下的文件和目录信息
#lst=os.listdir('chap15')        #FileNotFoundError: [WinError 3] 系统找不到指定的路径。: 'chap15'
lst=os.listdir('../chap15')     #退到上级目录
print(lst)
'''
['a.txt', 'b.txt', 'c.txt', 'copy2.png', 'copylogo.png', 'd.txt', 'demo1.py', 'demo10.py', 'demo11.py', 'demo12.py',
 'demo13.py', 'demo14.py', 'demo15.py', 'demo2.py', 'demo3.py', 'demo4.py', 'demo5.py', 'demo6.py', 'demo7.py', 
 'demo8.py', 'demo9.py', 'logo.png']
'''

#创建目录
#os.mkdir('newdir1')

#创建多级目录
#os.makedirs('A/B/C')

#删除目录
#os.rmdir('newdir1')

#删除多级目录
#os.removedirs('A/B/C')

#将path设置为当前的工作目录
#os.chdir('G:\\Python源码\\chap15')
#print(os.getcwd())
os.chdir('G:\\Python1\\chap15')
print(os.getcwd())

