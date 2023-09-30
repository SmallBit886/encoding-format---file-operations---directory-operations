#with语句，管理上下文
print(open('a.txt','r'))
'''<_io.TextIOWrapper name='a.txt' mode='r' encoding='cp936'>'''
'''这个类的对象open('a.txt','r')，称为上下文管理器'''
with open('a.txt','r') as file:
    print(file.read())  #不用手动关闭，自动关闭释放资源