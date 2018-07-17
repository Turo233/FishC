'''
import easygui as g
import os
import os.path

def folder_s(path, target, _types, code_type_row, code_type_folder):
   file_path = os.chdir(path)
   #改变路径
   for each_file in os.listdir(os.curdir):
      #判断是否是文件夹,是则递归
      if os.path.isdir(each_file):
         folder_s(path+os.sep+each_file, target, _types, code_type_row, code_type_folder)
         os.chdir(os.pardir)

#递归后返回上一级
      else:
         #对不是递归的项目进行类型统计
         try:
            (name, _type) = each_file.split('.', 1)
            if _type in target:
               _types.append(path+os.sep+each_file)
               #存储路径
               code_type_row.setdefault(_type, 0)
               #把类型放入字典,后续加入行数
               code_type_folder.setdefault(_type, 0)
               code_type_folder[_type] += 1
               #同上类型加入字典,并统计类型文件个数
         except:
            pass
   return (_types, code_type_row, code_type_folder)
#返回路径,类型数,类型文件个数

def calc_code(code_path):
   #统计单个文件行数并返回
   try:
      with open(code_path) as f:
         all_row = len(f.readline())
   except:
      with open(code_path, encoding ='UTF-8') as f1:
      all_row = len(f1.readline())
   return all_row

code_type_row = dict() #定义字典统计行数
code_type_folder = dict() #定义字典统计文件个数
_types = [] #定义列表统计路径

target = ['py', 'c', 'cpp', 'pas', 'asm']  #目标类型

folder_path = g.diropenbox(msg='请选择您的代码库:', title='浏览文件夹', default='E://编程')
(path, types, c_num) = folder_s(folder_path, target, _types, code_type_row, code_type_folder)

code_sum = 0 #已编码行数

for each in path:
   #统计各类型文件编码行数
   (name, __type) = each.split('.', 1)
   code_sum += calc_code(each)
   code_type_row[__type] += calc_code(each)

text_code = [] #最后显示文本

for each in code_type_row:
   text_code.append('【.%s】源文件%d个, 源代码%d行\n' % (each, code_type_folder[each], code_type_row[each]))

precent = code_sum / 1000
distant = 100000 - code_sum

g.textbox(msg='您目前共累计编写了%d行代码, 完成进度:%d %%\n离10万行代码还差%d行, 请继续努力!' %(code_sum, precent, distant), title='统计结果', text=text_code)
'''
import easygui as g
import os
import os.path

def calc_code(file_name):
   lines = 0
   with open(file_name) as f:
      print('正在分析文件:%s...' % file_name)
      try:
         lines = len(f.readline())
      except UnicodeDecodeError:
         pass
   return lines

def search_file(path):
   os.chdir(path)

   for each_file in os.listdir(os.curdir):
      ext = os.path.splitext(each_file)[1]
      if ext in target:
         lines = calc_code(each_file)
         try:
            file_list[ext] += 1
         except:
            file_list[ext] = 1
         try:
            source_list[ext] += lines
         except:
            source_list[ext] = lines
      if os.path.isdir(each_file):
         search_file(each_file)
         os.chdir(os.pardir)
def show_result(path):
   lines = 0
   total = 0
   text = ''

   for i in source_list:
      lines = source_list[i]
      total += lines
      text += '【 %s 】源文件 %d 个, 源代码 %d 行\n' % (i, file_list[i], lines)
   title = '统计结果'
   msg = '您目前共累计编写了%d行代码, 完成进度:%.2f %%\n离10万行代码还差%d行, 请继续努力!' % (total, total/1000, 100000-total)
   g.textbox(msg, title, text)

target = ['.py', '.c', '.cpp', '.pas', '.asm', '.java']
file_list = dict()
source_list = dict()

g.msgbox('请打开您存放所有代码的文件夹...', '统计代码量')
path = g.diropenbox('请选择您的代码库:')

search_file(path)
show_result(path)
