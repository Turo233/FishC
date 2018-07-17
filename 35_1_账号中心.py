#太杂乱了.
'''
import easygui as g

def input_information():
        items = g.multenterbox(msg='[*用户名]为必填项\n[*真实姓名]为必填项\n[*手机号码]为必填项\n[*E-mail]为必填项',title='账号中心',fields=('*用户名', '*真实姓名', '固定号码', '*手机号码', 'QQ', '*E-mail') )
        while items[0] == '' or items[1] == '' or items[3] == '' or items[5] == '':
                g.msgbox(msg='不可以,*后的值必须要填:', ok_button='返回')
                items = g.multenterbox(msg='[*用户名]为必填项\n[*真实姓名]为必填项\n[*手机号码]为必填项\n[*E-mail]为必填项',title='账号中心',fields=('*用户名', '*真实姓名', '固定号码', '*手机号码', 'QQ', 'E-mail') )
        return items

information = input_information()
for each in information:
        if each.isspace():
                g.msgbox(msg='NONONO!,请不要输入空格充数!', ok_button='continue')
                information = input_information()
                continue
while 1:        
        if information[2].isdigit() and information[3].isdigit() and information[4].isdigit():
                break
        else:
                g.msgbox(msg='请把电话或者qq号写成数字', ok_button='continue')
                information = input_information()
'''
import easygui as g

msg = '请填写联系方式'
title = '账号中心'
fieldNames = [' *用户名', ' *真实姓名', '  固定电话', ' *手机号码', '  QQ', ' *E-mail']
fieldValues = []
fieldValues = g.multenterbox(msg, title, fieldNames)

while 1:
        if fieldValues == None:
                break
        errmsg = ''
        for i in range(len(fieldNames)):
                option = fieldNames[i].strip()
                if fieldValues[i].strip() == '' and option[0] == '*':
                        errmsg += ('【%s】为必填项.\n\n' % fieldNames[i])
        if errmsg == '':
                break
        fieldValues = g.multenterbox(errmsg, title, fieldNames, fieldValues)
print('用户资料如下: %s' % str(fieldValues))        
