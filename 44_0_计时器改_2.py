import time as t

class MyTimer():
    def __init__(self):
        self.time = 0
        self.begin = 0
        self.end = 0
        self.prompt = '还未开始计时'

    def __add__(self, other):
        prompt = '总共运行了'
        result = 0
        result = self.end - self.begin
        if result:
            prompt += str(result)
        return prompt
    
    def __str__(self):
        return self.prompt
    __repr__ = __str__
    
    def start(self):
        self.begin = t.process_time()
        self.prompt = '提示: 请使用stop停止计时!'
        print('计时开始!')
        
    def stop(self):
        for i in range(100):
            pass
        if not self.begin:
            print('提示: 请使用start开始计时!')
        else:
            self.end = t.process_time()
            self._calc()
            print('计时结束!')
    
    def _calc(self):
        self.prompt = '总共运行了'
        self.time = self.end - self.begin
        self.prompt += str(self.time)
