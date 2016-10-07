RESPONSE_READ_ = '''
#values = {"username":"2151154","password":"cpf520you"}
#data = urllib.urlencode(values)
#rs = 3094315

url = "http://www.ncbi.nlm.nih.gov/genome/?term=rs3094315"
request = urllib2.Request(url)
response = urllib2.urlopen(request)
print response.read()

'''


__author__ = 'pigeon'
import urllib
import urllib2
import re

file = open("C:\\data.txt")
lines = file.readlines()
file.close()

for line in lines:
        line = line.strip('\n')
        url = 'http://www.ncbi.nlm.nih.gov/genome/?term=rs' + line
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        headers = { 'User-Agent' : user_agent }
        request = urllib2.Request(url, headers = headers)
        response = urllib2.urlopen(request)
        content = response.read().decode('utf-8')
        pattern = re.compile('<p class="desc">.*\.')
        items = re.findall(pattern, content)
        print items



'''
        try:
         request = urllib2.Request(url, headers = headers)
         response = urllib2.urlopen(request)
         content = response.read().decode('utf-8')

         pattern = re.compile('<p class="desc">.*\.')
         items = re.findall(pattern, content)
         print items

        except urllib2.URLError, e:
         if hasattr(e,"code"):
            print e.code
         if hasattr(e,"reason"):
            print e.reason


'''