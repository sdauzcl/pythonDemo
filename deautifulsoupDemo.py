from bs4 import BeautifulSoup
import re
import warnings
warnings.filterwarnings("ignore")

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tilcie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

soup = BeautifulSoup(html)
#print(soup)
print(soup.a)
print(soup.a.attrs)#{'href': 'http://example.com/elsie', 'class': ['sister'], 'id': 'link1'}

print(soup.a.string)
all = soup.find_all('a')
print(all)
print('---')
i = 0
# for child in soup.body.children:
#     print(i)
#     print(child)
#     i = i+1
# print('++++')
for x in all:
    #print(x.name)
    print(BeautifulSoup(str(x)).a.string)
print(soup.find_all(id="link1"))
print(soup.find_all(id=re.compile('^link')))
#print(soup.find_all('p',class_ = 'story'))

print(soup.find_all(text=re.compile('cie')))


print(soup.select('a'))
print(soup.select('.sister'))
print(soup.select('#link1')[0].string)




