#snake

import turtle

def drawSnake(rad, angle, len, neckrad):
    for i in range(len):
        turtle.circle(rad, angle)       #rad描述圆形轨迹半径的位置，半径为负值，则半径在小乌龟右侧
        turtle.circle(-rad, angle)      #angle 表示小乌龟沿着圆形爬行的弧度值
    turtle.circle(rad, angle/2)         
    turtle.fd(rad)                      #也叫turtle.forward()表示乌龟向前爬行，有个参数表示爬行距离
    turtle.circle(neckrad+1,180)
    turtle.fd(rad*2/3)
    
def main():
    turtle.setup(1800, 800, 0, 0)       #绘图窗口像素（长，宽，左上角坐标）
    pythonsize = 30
    turtle.pensize(pythonsize)          #乌龟宽度
    turtle.pencolor("blue")             #乌龟颜色
    turtle.seth(-40)                    #爬行角度（垂直坐标系）
    drawSnake(40, 80, 5, pythonsize/2)   #参数传递

main()
