#课堂案例2
#遍历指定目录下的所有文件及其子文件
import os
#os.mkdir('newdir1')

path=os.getcwd()
print(path) #G:\Python1\chap15
print('*******************')
lst_file=os.walk(path)
print(lst_file) #<generator object _walk at 0x00000296E1D44320>
for dirpath,dirname,filename in lst_file:
    for dir in dirname:
        print(os.path.join(dirpath,dir))

    for file in filename:
        print(os.path.join(dirpath,file))
''' print(dirpath)
    print(dirname)
    print(filename)
    print('--------------------------------')
'''
'''G:\Python1\chap15
['newdir1']
['a.txt', 'b.txt', 'c.txt', 'copy2.png', 'copylogo.png', 'd.txt', 'demo1.py', 'demo10.py', 'demo11.py', 'demo12.py', 'demo13.py', 'demo14.py', 'demo15.py', 'demo16.py', 'demo17.py', 'demo18.py', 'demo2.py', 'demo3.py', 'demo4.py', 'demo5.py', 'demo6.py', 'demo7.py', 'demo8.py', 'demo9.py', 'logo.png']
--------------------------------
G:\Python1\chap15\newdir1
['su']
['1.py', '2.py']
--------------------------------
G:\Python1\chap15\newdir1\su
[]
['sub1.py']
--------------------------------
'''

