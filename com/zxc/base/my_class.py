#!/usr/bin/env python3     
# -*- coding: utf-8 -*-  
# create by zhuxc@joyowo.com
# 2017/8/21

class Emp:
    """员工基类"""
    empCount = 0

    """类方法第一个参数必须为self，指向当前类的实例。可以换成别的名字"""

    def __init__(self, name, age):
        # 添加新属性
        self.name = name
        self.age = age
        Emp.empCount += 1

    def showCount(self):
        print("count is %d" % Emp.empCount)
        return

    def showEmp(instance):
        print("name:", instance.name, "age:", instance.age)
        del instance.age  # 删除age属性
        print("name:", instance.name)
        return

    def showClsInfo(self):
        print("id:", id(self))
        print(Emp.__dict__)
        print(Emp.__doc__)
        print(Emp.__name__)
        print(Emp.__module__)
        print(Emp.__bases__)


emp = Emp(name="jack", age=17)
emp.showCount()
emp.showEmp()
emp.showClsInfo()


class Vector:
    """运算符重载"""

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)


v1 = Vector(2, 10)
v2 = Vector(5, -2)
print(v1 + v2)
