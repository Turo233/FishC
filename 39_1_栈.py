class Stack:
        def __init__(self, start=[]):
                self.stack = []
                for x in start:
                        self.push(x)
                        
        def isEmpty(self):
                return not self.stack
        
        def push(self, data):
                self.content.append(data)
                
        def pop(self):
                try:
                        self.content.pop()
                except AttributeError:
                        print('警告, 栈为空')
        def top(self):
                try:
                        print(self.content[-1])
                except AttributeError:
                        print('警告, 栈为空')
        def bottom(self):
                try:
                        print(self.content[0])
                except AttributeError:
                        print('警告, 栈为空')
