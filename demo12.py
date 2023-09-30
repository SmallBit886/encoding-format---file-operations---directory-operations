#
'''MyContentMgr实现了特殊方法，__enter__(),__exit__()称为该类对象遵守了上下文管理器协议
MyContentMgr()该类对象的实例对象，称为上下文管理器
'''
class MyContentMgr(object):
    def __enter__(self):
        print('enter方法被调用执行了')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit方法被执行了')

    def show(self):
        print('show方法被调用执行了',1/0)

with MyContentMgr() as file:
    file.show()
'''enter方法被调用执行了
show方法被调用执行了
exit方法被执行了'''
#产生异常
'''ZeroDivisionError: division by zero
enter方法被调用执行了
exit方法被执行了'''