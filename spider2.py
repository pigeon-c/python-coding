'''
while 1:
    line = file.readline()
    if not line:
        break
    print line
'''


__author__ = 'pigeon'


file = open("C:\\data.txt", 'r')

lines = file.readlines()

file.close()

for line in lines:
        line = line.strip('\n')
        print line
        print len(line)
