import re
import urllib.request as ur
from bs4 import BeautifulSoup
import chardet
def get_link():
   url = 'https://baike.baidu.com/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB'
   response = ur.urlopen(url)
   html = response.read()
   encode = chardet.detect(html)['encoding']
   if encode == 'GB2312':
      encode = 'GBK'
      
   html = html.decode(encode, 'ignore')

   soup = BeautifulSoup(html, 'html.parser')

   link = soup.find_all(href=re.compile('view'))

   for each in link:
      print(each.get('title'), '->', r'https://baike.baidu.com'+each.get('href'))
      
if __name__ == '__main__':
   get_link()
