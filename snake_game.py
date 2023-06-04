import pygame
import sys
import setting

# 初始化蛇和食物
snake = Snake(width // 2, height // 2)
food = Food()


start_screen()
game_loop()
