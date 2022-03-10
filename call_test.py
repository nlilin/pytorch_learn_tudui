class Persion:
    def hello(self,name):
        print("hello"+name)

    #__call__内置函数，不用调用方法
    def __call__(self,name):
        print("__call__"+"hello"+name)

persion=Persion()
persion("zhangsan")
persion.hello("lisi")