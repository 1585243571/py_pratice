#!/usr/bin/python3 

class MyClass:
    __v='aaaaaaa'#定义私有变量
    a=0;b=12 #定义共有的静态成员变量，类似与c++的static int a静态成员变量上面为静态私有变量，可供类的对象共享
    def get(self):
        return self.__v
    def print_date(self):
        print("aaa")
        #self.l=13 错误的做法成员变量只能在构造函数中定义
    def __init__(self):
        self.m=12  #定义共有的成员变量
        #print(self)
        print(self.m)
        print('object count:',MyClass.a)
        MyClass.a=MyClass.a+1
        #print(self.__class__)
        print(self.__v)#私有变量只能通过self.来访



a=MyClass()
a.a=23;
b=MyClass()
print(b.a)
print(a.l)
