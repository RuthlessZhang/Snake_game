import setting
import pygame


# 食物类定义

class Food:
    def __init__(self):
        self.block = self.generate_block()

    def generate_block(self):
        x = random.randint(0, width // block_size - 1) * block_size
        y = random.randint(0, height // block_size - 1) * block_size
        return x, y

    def draw(self):
        pygame.draw.rect(screen, red, (self.block[0], self.block[1], block_size, block_size))

    def update_speed(self):
        if self.speed < self.max_speed:
            self.speed += 2

