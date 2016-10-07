#coding=utf-8
#第一行加上上面  才可以中文注释  不然会报错
__author__ = 'pigeon'










student = {'xiaoming': 20, 'feige': 22, 'xiaohong': 23 }
print student['feige']

#修改
student['feige'] = 24
print student

#增加
student['hello'] = 'world'
print student

#删除字典元素
del student['xiaoming']
print student

if __author__ == 'pigeon':
    print __author__


#del student  删除字典