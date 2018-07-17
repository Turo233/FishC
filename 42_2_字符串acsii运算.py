# I love FishC.com!
class Duck:
    def quack(self): 
        print("呱呱呱！")
    def feathers(self): 
        print("这个鸭子拥有灰白灰白的羽毛。")

class Person(Duck):
    def a(self):
        print("你才是鸭子你们全家人是鸭子！")
    def b(self): 
        print("这个人穿着一件鸭绒大衣。")




print(Person().quack())
