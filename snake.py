import setting
import pygame


# 蛇类定义
class Snake:
    def __init__(self, x, y):
        self.body = [(x, y)]
        self.direction = "right"
        self.score = 0
        self.high_score = 0
        self.speed = 10
        self.max_speed = 30
        self.timer = 0

    def move(self):
        if self.direction == "up":
            new_block = (self.body[0][0], self.body[0][1] - block_size)
        elif self.direction == "down":
            new_block = (self.body[0][0], self.body[0][1] + block_size)
        elif self.direction == "left":
            new_block = (self.body[0][0] - block_size, self.body[0][1])
        elif self.direction == "right":
            new_block = (self.body[0][0] + block_size, self.body[0][1])

        self.body.insert(0, new_block)
        self.body.pop()

    def grow(self):
        last_block = self.body[-1]
        if self.direction == "up":
            new_block = (last_block[0], last_block[1] + block_size)
        elif self.direction == "down":
            new_block = (last_block[0], last_block[1] - block_size)
        elif self.direction == "left":
            new_block = (last_block[0] + block_size, last_block[1])
        elif self.direction == "right":
            new_block = (last_block[0] - block_size, last_block[1])

        self.body.append(new_block)
        self.score += 10

    def draw(self):
        for block in self.body:
            pygame.draw.rect(screen, white, (block[0], block[1], block_size, block_size))

            # 绘制得分和历史最高分
            font = pygame.font.Font(None, 30)
            text1 = font.render("Score: {}".format(self.score), True, white)
            screen.blit(text1, (10, 10))

            text2 = font.render("High Score: {}".format(self.high_score), True, white)
            screen.blit(text2, (10, 40))


# 在 Snake 类中添加长按方向键加速的处理
"""def handle_event(self, event):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP and self.direction != "down":
            self.direction = "up"
        elif event.key == pygame.K_DOWN and self.direction != "up":
            self.direction = "down"
        elif event.key == pygame.K_LEFT and self.direction != "right":
            self.direction = "left"
        elif event.key == pygame.K_RIGHT and self.direction != "left":
            self.direction = "right"

        # 累计时间，并检查是否超过阈值
        self.timer += 1
        if self.timer >= 10:
            self.update_speed()
            self.timer = 0
    elif event.type == pygame.KEYUP:
        # 重置计时器
        self.timer = 0"""
