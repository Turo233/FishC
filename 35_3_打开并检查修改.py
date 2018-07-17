import easygui as g
import os

file_path = g.fileopenbox(default='F:/编程/', filetypes=['*.txt'])
'''
text = open(file_path)
content = text.read()
text.close()
'''
#with 用法
with open(file_path) as old_file:
   title = os.path.basename(file_path)
   msg = '文件【%s】的内容如下:' % file_path
   text = old_file.read()
   text_after = g.textbox(msg, title, text)


   if text != text_after[:-1]:
      #textbox的返回值会追加一个换行符
      choice = g.buttonbox(msg='检测到文件内容发生改变,请选择以下操作:', title='警告', choices=('覆盖保存', '放弃保存', '另存为...'))
      if choice == '覆盖保存':
        with open(file_path, 'w') as old_file:
           old_file.write(content_2)
           
      if choice == '另存为...':
         another_path = g.filesavebox(default='.txt')
         if os.path.splitext(another_path)[1] != '.txt':
            another.path += '.txt'
         with open(text_2_path, 'w') as new_file:
            new_file.write(text_after[:-1])
            
      if choice == '放弃保存':
         pass
         
