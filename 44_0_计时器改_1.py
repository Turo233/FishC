import time as t

class MyTimer():
    def __init__(self):
        self.unit = ['年', '月', '天', '小时', '分', '秒']
        self.last = []
        self.begin = 0
        self.end = 0
        self.prompt = '还未开始计时'

    def __add__(self, other):
        prompt = '总共运行了'
        result = []
        for index in range(6):
            result.append(self.last[index] + other.last[index])
            if result[index]:
                prompt += (str(result[index]) + self.unit[index])
        return prompt
    def __str__(self):
        return self.prompt
    __repr__ = __str__
    
    def start(self):
        self.begin = t.localtime()
        self.prompt = '提示: 请使用stop停止计时!'
        print('计时开始!')
        
    def stop(self):
        if not self.begin:
            print('提示: 请使用start开始计时!')
        else:
            self.end = t.localtime()
            self._calc()
            print('计时结束!')
    
    def _calc(self):
        self.prompt = '总共运行了'
        self.last = []
        for index in range(6):
            self.last.append(self.end[index] - self.begin[index])

        if self.last[5] < 0:
            self.last[5] += 60
            self.last[4] -= 1
        if self.last[4] < 0:
            self.last[4] += 60
            self.last[3] -= 1
        if self.last[3] < 0:
            self.last[3] += 12
            self.last[2] -= 1
        if self.last[2] < 0:
            self.last[2] += 31
            self.last[1] -= 1
        if self.last[1] < 0:
            self.last[1] += 12
            self.last[0] -= 1
            
        for index in range(6):
            if self.last[index]:
                self.prompt += (str(self.last[index]) + self.unit[index])
