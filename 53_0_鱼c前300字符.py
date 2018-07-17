import urllib.request
import chardet

Fishc = urllib.request.urlopen('http://www.FishC.com').read()
coding = chardet.detect(Fishc)['encoding']
Fishc = Fishc.decode(coding)
print(Fishc[:300])
