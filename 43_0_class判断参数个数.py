class C:
    def __init__(self, *param):
        if not param:
            print('并没有传入参数')
        else:
            print('传入了 %d 个参数, 分别是:'%len(param), param)
