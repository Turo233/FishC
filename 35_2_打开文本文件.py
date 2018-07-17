import easygui as g
import os.path

file_path = g.fileopenbox(default='F:/编程', filetypes=['*.txt'])
'''
text = open(file_path)
content = text.read()
'''
#为什么把with open() as A:忘掉了!!

with open(file_path) as f:
   content = f.read()
   title = os.path.basename(file_path)
   msg = '文件【%s】的内容如下:' % title
   
   g.textbox(msg, title, content)


