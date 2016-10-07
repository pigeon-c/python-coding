#coding=utf-8
__author__ = 'Pigeon'
'''


'''

#双引号内需要双斜杠  单引号需要但斜杠

file = open('C:\\123.txt')
fileout = open('C:\\pigeon.txt', 'r+')

#一次读取所有的行  存放在列表中 列表中的元素是字符串  然后关闭文件
lines = file.readlines()
file.close()


#在列表的元素中遍历  类型是字符串
for line in lines:
        line = line.strip('\n')  #去除读取行末尾的换行符
        if len(line) > 10:
            print line
            fileout.writelines(line+'\n')   #分号被去除了   这里所有的都在同一行






fileout.close()

#lines 类型是
print type(lines)
print type(line)


