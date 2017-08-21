#!/usr/bin/env python3     
# -*- coding: utf-8 -*-  
# create by zhuxc@joyowo.com
# 2017/8/21

def changeList(mylist):
    """
        修改mylist
        传可变参数（list, dict）使用的是引用本身，改变引用数据会发生变化
    """
    mylist.append([1, 2, 3, 4])
    print("函数内值：", mylist)
    return


def changeConstant(param):
    """
        修改param
        传不可变参数（string, number, tuple）使用的是引用所指向的值，改变引用原值不会发生变化
    """
    param = 13
    print("函数内param", param)
    return


mylist = [10, 20, 30]
changeList(mylist)
print("函数外值：", mylist)

mylist = 1
changeConstant(mylist)
print("函数外param：", mylist)


def printme(str, age):
    """传入cans"""
    print("str:", str, "age:", age)
    return


printme("jjj", "ddd")
# 这种传法需要和方法中参数名一致
printme(age=12, str="kk")


def printinfo(arg1, *args):
    print("arg1:", arg1)
    """ *表示未命名的所有可变参数 """
    print("length of args:", len(args))
    print("============")
    for arg in args:
        print(arg, end=", ")  # 打印不换行,end内容自定义
    return


printinfo("hello", 18, "kk", [19, 78, "hfdhj"])
