import time as t
import os
import os.path

class MyDes:
        record = []
        def __init__(self):
                with open(r'F:\编程\python\record.txt', 'w') as F:
                        for each in self.record:
                                F.write(each+'\n')
                
class Record:
        time = t.strftime('%a %b %d %H:%M:%S %Y', t.localtime()) 

        def __init__(self, value=None, var=None):
                self.record = []
                self.value = value
                self.var = var
                

        def __get__(self, intance, owner):
                MyDes.record.append('%s变量于北京时间 '%self.var + self.time + '被读取，%s = %s' %(self.var, self.value))
                MyDes()
                return self.value
        
        def __set__(self, instance, value):
                self.value = value
                MyDes.record.append('%s变量于北京时间 '%self.var + self.time + '被修改，%s = %s' %(self.var, self.value))
                MyDes()
                
class Test:
	x = Record(10, 'x')
	y = Record(8.8, 'y')

test = Test()
