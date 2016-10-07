#coding=utf-8
__author__ = '小飞鸽'


x = 123
y = 234
z = 1

#这是一个无参函数的定义   无返回值 默认返回None   内部x没申明不影响全局变量x
def fun_1():
    print '================================================='
    print 'This is the function one'
    x = 1    #局部变量x     并没有改变全局变量x的值
    print 'fun_1中变量x=%d' % x
    print '================================================='




#调用全局变量  并返回一个值
def fun_2():
    print '================================================='
    print 'Yhis is the function two'
    global x
    #显示x引用值的内容 是一个地址
    print id(x)
    x = 1    #局部变量x   并没有改变全局变量x的值
    print id(x)

    print 'fun_2中变量x=%d' % x
    print '================================================='
    return x



#注意  python函数传递的是引用   但是其不会改变实参的值
def fun_3(x, y):
    print '================================================='
    print 'Yhis is the function 3'

    print id(x)
    print id(y)

    x = 1345
    y = y + 1
    z = x + y
    print id(x)
    print id(y)

    print 'fun_2中变量z=%d' % z
    print '================================================='
    return z



print id(x)
print id(y)
print id(z)


#调用函数  没有声明x为全局变量  不改变全局变量x的值
print fun_1()
print '全局变量x=%d' % x


#调用函数2
print fun_2()
print '全局变量x=%d' % x



#调用函数3
print fun_3(x,y)
print "y 的值 = %d" % y