# -*- coding: utf-8 -*-



# __new__与__init__
class myClass():
    def __new__(cls, *args):  # 如果__new__函数不返回任何对象，则__init__函数也不会被调用。
        print("__new__ is called")
        # return super(myClass, cls).__new__(cls)

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        print("name is: %s and gender is: %s." % (self.name, self.gender))


myClass('HHF', 'Male')




# 私有变量
class Student():  # 不带()也可以
    def __init__(self, name, score):
        self.__name = name  # 私有变量
        self.__score = score
        print('My name is %s, score is %0.2f.' % (self.__name, self.__score))


s = Student('HHF', 98.234)
s.gender = 'Male'  # 动态地给实例绑定一个属性
# Python解释器对外吧__name变量变成了__Student_name，所以仍然可以通过_Student__name来访问_name变量
print(s._Student__name, s.gender)




# MethodType的使用
from types import MethodType

class Student():
    pass
def set_name(self, name):
    self.name = name
s1 = Student()
s2 = Student()
s1.set_name = MethodType(set_name, s1)  # 给实例绑定一个方法
s1.set_name('Tom')
# s2.set_name('Jack')  # AttributeError: 'Student' object has no attribute 'setNmae'
print(s1.name)

class Stu():
    pass
def set_age(self,age):
    self.age = age
# Stu.set_age = MethodType(set_age, Stu)  # 给类绑定一个方法
Stu.set_age = set_age
A = Stu()
B = Stu()
C = Stu()
A.set_age(10)
B.set_age(15)
print(A.age, B.age, C.age)  # 结果都是15




# __slots__限制实例能添加的属性
class Student():
    __slots__ = ('name', 'age')
s = Student()
s.name = "Jack"  # 绑定属性'name'
s.age = 25  # 绑定属性'age'
# s.gender = 'Male'  # 绑定属性'gender' # AttributeError: 'Student' object has no attribute 'gender'

class Person(Student):
    # __slots__ = ('score')
    pass
a = Person()
a.age = 21
a.score = 96
a.gender = 'Female'  # 若前面加上__slots__ = ('score')，则AttributeError: 'Person' object has no attribute 'gender'




# 枚举类
from enum import Enum

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)  # Jan => Month.Jan , 1……  # value属性则是自动赋给成员的int常量，默认从1开始计数。
    

    
    
# 多继承的__mro__方法
class Base:
    def __init__(self):
        print('Base.__init__')

class A(Base):
    def __init__(self):
        super().__init__()
        print('A.__init__')

class B(Base):
    def __init__(self):
        super().__init__()
        print('B.__init__')

class C(A,B):
    def __init__(self):
        super().__init__()  # Only one call to super() here
        print('C.__init__')

c = C() # 必须加()
print(C.__mro__)  # (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class '__main__.Base'>, <class 'object'>)
