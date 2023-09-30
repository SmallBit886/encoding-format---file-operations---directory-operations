#os.path模块操作目录相关函数
import os.path
'''用于获取目录或者文件的绝对路径'''
print(os.path.abspath('demo13.py')) #G:\Python1\chap15\demo13.py

'''用于判断文件或者目录是否存在'''
print(os.path.exists('demo13.py'),os.path.exists('demo18.py'))  #True False

'''将目录与目录或者文件名拼接起来'''
#print(os.path.join('E:\\python','demo13.py'))   #E:\python\demo13.py

'''将目录与文件拆分'''
print(os.path.split('E:\\vippython\\chap15\\demo13.py'))    #('E:\\vippython\\chap15', 'demo13.py')

'''将文件名字和文件的后缀名分开'''
print(os.path.splitext('demo13.py'))    #('demo13','py')

'''从一个目录中提取文件名'''
print(os.path.basename('G:\\Python1\\chap15\\demo13.py'))   #demo13.py

'''从一个路径中提取文件路径，不包括文件名'''
print(os.path.dirname('G:\\Python1\\chap15\\demo13.py'))    #G:\Python1\chap15

'''用于判断是否为路径'''
print(os.path.isdir('G:\\Python1\\chap15\\demo13.py'))  #False
print(os.path.dirname('G:\\Python1\\chap15'))   #G:\Python1
print(os.path.dirname('G:\\Python1'))   #G:\