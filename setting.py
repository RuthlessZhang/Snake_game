# 定义游戏区域参数
block_size = 12
width = 80 * block_size
height = 60 * block_size

# 定义颜色
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)


class Settings:
    def __init__(self):
        self.block_size = block_size
        self.width = width
        self.height = height

        self.white = white
        self.black = black
        self.green = green
        self.red = red
