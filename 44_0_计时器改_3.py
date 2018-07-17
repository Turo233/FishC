import time as t

class MyTimer:
    
    def __init__(self, file, count=1000000):
        self.count = count
        self.file = file
        self.time = 0
        self.begin = 0
        self.end = 0
        self.prompt = '还未开始计时'

    def __add__(self, other):
        prompt = '总共运行了'
        result = 0
        result = (self.time + other.time)
        if result:
            prompt += ('%.2f'%result + str('秒'))
        return prompt
    
    def __str__(self):
        return self.prompt
    __repr__ = __str__

    def timing(self):
        self._start()
        for times in range(self.count):
            self.file()
        self._stop()
        
    def _start(self):
        self.begin = t.process_time()
        
    def _stop(self):
        self.end = t.process_time()
        self._calc()
    
    def _calc(self):
        self.prompt = '总共运行了'
        self.time = self.end - self.begin
        self.prompt += ('%.2f'%self.time + str('秒'))
