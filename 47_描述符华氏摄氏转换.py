class Celsius:
        def __init__(self, temp=26.0):
                self.temp = temp
        def __get__(self, instance, owner):
                return self.temp
        def __set__(self, instance, value):
                self.temp = float(value)

class Fahrenheit:
        def __get__(self, instance, owner):
                return instance.cel * 1.8 + 32
        def __set__(self, instance, value):
                instance.cel = (float(value) - 32) / 1.8
                
class Temperature:
        cel = Celsius()
        fah = Fahrenheit()
