# -*- coding: utf-8 -*-

import logging


def use_logging(func):
    logging.warning("%s is running" % func.__name__)
    func()

def foo():
    print('i am foo')

use_logging(foo)
# OUTPUT
# i am foo
# WARNING:root:foo is running

# 我们调用的时候不再是调用真正的业务逻辑 foo 函数，而是换成了 use_logging 函数，这就破坏了原有的代码结构




# 简单装饰器
def use_logging(func):
    def wrapper():
        logging.warning("%s is running" % func.__name__)
        return func()   # 把 foo 当做参数传递进来时，执行func()就相当于执行foo()
    return wrapper

def foo():
    print('i am foo')

foo = use_logging(foo)  # 因为装饰器 use_logging(foo) 返回的是函数对象 wrapper，这条语句相当于  foo = wrapper
foo()                   # 执行foo()就相当于执行 wrapper()




# 语法糖@
def use_logging(func):
    def wrapper():
        logging.warning("%s is running" % func.__name__)
        return func()
    return wrapper

@use_logging  # 放在函数开始定义的地方，这样就可以省略最后一步再次赋值的操作
def foo():
    print("i am foo")

foo()
# OUTPUT
# i am foo
# WARNING:root:foo is running




# 如果业务逻辑函数 foo 需要参数，可以在定义 wrapper 函数的时候指定参数
def use_logging(func):
    def wrapper(*args, **kwargs):
        logging.warning("%s is running" % func.__name__)
        return func(*args, **kwargs)
    return wrapper

@use_logging
def foo(name, age=None, height=None):
    print("I am %s, age %s, height %s" % (name, age, height))

foo('HHF', '26', '176cm')
# OUTPUT
# WARNING:root:foo is running
# i am HHF




# 带参数的装饰器
def use_logging(level):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if level == "warn":
                logging.warning("WARNING %s is running" % func.__name__)
            elif level == "info":
                logging.info("INFO %s is running" % func.__name__)
            return func(*args)
        return wrapper

    return decorator

@use_logging(level="warn")
def foo(name='foo'):
    print("i am %s" % name)

foo()
# OUTPUT
# i am foo
# WARNING:root:WARNING foo is running




# 类装饰器
class Foo():
    def __init__(self, func):
        self._func = func
    def __call__(self):
        print ('class decorator runing')
        self._func()
        print ('class decorator ending')

@Foo
def bar():
    print ('bar')

bar()
# OUTPUT
# class decorator runing
# bar
# class decorator ending




# functools.wraps
# wraps本身也是一个装饰器，它能把原函数的元信息拷贝到装饰器里面的 func 函数中，这使得装饰器里面的 func 函数也有和原函数 foo 一样的元信息了
from functools import wraps
def logged(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__)      # 输出 'f'
        print(func.__doc__)       # 输出 'does some math'
        return func(*args, **kwargs)
    return with_logging

@logged
def f(x):
   """does some math"""
   print(x + x * x)

f(3)
# OUTPUT
# f
# does some math
# 12




# 装饰器顺序
# 一个函数还可以同时定义多个装饰器，它的执行顺序是从里到外，最先调用最里层的装饰器，最后调用最外层的装饰器
@a
@b
@c
def f ():
    pass
# 等效于f = a(b(c(f)))
