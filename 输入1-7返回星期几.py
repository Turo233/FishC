#1-7返回星期几

weeks = "星期一星期二星期三星期四星期五星期六星期日"

n = input("请输入星期数(1-7):")
pos = (int(n)-1) * 3

weekabbrev = weeks[pos:pos+3]
print("今天是"+weekabbrev+".")
