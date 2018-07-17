import urllib.request
import chardet

def detecturl():
   url = input('请输入URL : ')
   Ocontent = urllib.request.urlopen(url).read()
   coding = chardet.detect(Ocontent)['encoding']
   print('该网页使用的编码是 : ', coding)

if __name__ == '__main__':
   detecturl()
