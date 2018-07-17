import urllib.request
import chardet
import easygui as g

def mao():
   title = '猫片下载'
   g.msgbox('欢迎使用猫片下载器', title)

   msg = '请填写喵的尺寸'
   fildNames = ['宽', '高']
   fildValues = g.multenterbox(msg, title, fildNames)
   
   url = r'http://placekitten.com/g/%s/%s'%(fildValues[0], fildValues[1])

   response = urllib.request.urlopen(url).read()
   
   path = r'F:/jpg/%s_%s的猫片.jpg'%(fildValues[0], fildValues[1])
   savepath = g.filesavebox('请选择存放猫片的位置', default=path, filetypes=['*.jpg'])

   with open(savepath, 'wb') as f:
      f.write(response)
   
if __name__ == '__main__':
   mao()
