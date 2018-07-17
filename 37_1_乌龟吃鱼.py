import random

#设置区域范围
legal_x = [0, 10]
legal_y = [0, 10]
class Turtle:
    
    life = 100
    #乌龟随机初始位置
    pos_x = random.randint(0, 10)
    pos_y = random.randint(0, 10)
    def moving(self):
        #随机步伐
        self.step = random.randint(1, 2)
        self.new_x = self.pos_x
        self.new_y = self.pos_y
        
        #判定每一次是x方向还是y方向并移动.
        for i in range(self.step):
            direction = random.randrange(-1, 2, 2)
            #-1为左(下) 1为右(上)
            choices = ('x', 'y')
            xy = random.choice(choices)
            if xy == 'x':
                self.new_x = self.pos_x + direction
            if xy == 'y':
                self.new_y = self.pos_y + direction
        
        if self.new_x < legal_x[0]:
            self.pos_x = legal_x[0] - (self.new_x - legal_x[0])
        elif self.new_x > legal_x[1]:
            self.pos_x = legal_x[1] - (self.new_x - legal_x[1])
        else:
            self.pos_x = self.new_x

        if self.new_y < legal_y[0]:
            self.pos_y = legal_y[0] - (self.new_y - legal_y[0])
        elif self.new_y > legal_y[1]:
            self.pos_y = legal_y[1] - (self.new_y - legal_y[1])
        else:
            self.pos_y = self.new_y
            self.life -= self.step
        return (self.pos_x, self.pos_y)
    def eat(self):
        self.life += 20
        if self.life > 100:
            self.life = 100


class Fish:
    legal_x = [0, 10]
    legal_y = [0, 10]
    pos_x = random.randint(0, 10)
    pos_y = random.randint(0, 10)
    def moving(self):
        self.new_x = self.pos_x
        self.new_y = self.pos_y
        self.step = 1
        for i in range(self.step):
            direction = random.randrange(-1, 2, 2)
            choices = ('x', 'y')
            xy = random.choice(choices)
            if xy == 'x':
                self.new_x = self.pos_x + direction
            if xy == 'y':
                self.new_y = self.pos_y + direction
        
        if self.new_x < legal_x[0]:
            self.pos_x = legal_x[0] - (self.new_x - legal_x[0])
        elif self.new_x > legal_x[1]:
            self.pos_x = legal_x[1] - (self.new_x - legal_x[1])
        else:
            self.pos_x = self.new_x

        if self.new_y < legal_y[0]:
            self.pos_y = legal_y[0] - (self.new_y - legal_y[0])
        elif self.new_y > legal_y[1]:
            self.pos_y = legal_y[1] - (self.new_y - legal_y[1])
        else:
            self.pos_y = self.new_y
        return (self.pos_x, self.pos_y)

player = Turtle()
fish_num = dict()
fish_posxy = dict()

for i in range(10):
    fish_num[i] = Fish()
while 1:
    player.moving()
    #将十条鱼的随机位置存储在字典里
    
    for each in fish_num:
        fish_num[each].moving()
        fish_posxy[each] = [fish_num[each].pos_x, fish_num[each].pos_y]
    player_xy = [player.pos_x, player.pos_y]
    '''
    #看位置信息是否正确
    for each in fish_posxy:
        print(fish_posxy[each], end=' ')
    print('\n')
    print(player_xy)
    print('\n')
    '''

    #遍历鱼位置字典查找与乌龟相同位置的鱼并加命和删除鱼
    fish_del = list(fish_num.keys())
    for each in fish_del:
        if fish_posxy[each] == player_xy:
            player.eat()
            del fish_num[each]  #做笔记, 又忘了字典中删除是remove还是del, 需要重新回顾字典的函数
            print('有一条鱼被吃掉了')
    '''      
    for each in fish_num:
        print(fish_posxy[each], end=' ')
        
    print('\n')
    print(player_xy)
    print('\n')
    '''

    if player.life > 0 and not fish_num:
        print('NICE !! Turtle is win!')
        break
    if player.life <= 0 or not fish_num:
        print('没命了..game over')
        break
    
        

        
     
