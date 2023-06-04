import setting
import pygame


def game_loop():

    # 游戏主循环
    game_over = False
    clock = pygame.time.Clock()

    # 初始化速度和速度上限
    speed = 10
    max_speed = 30

    while not game_over:
        # 处理事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake.direction != "down":
                    snake.direction = "up"
                elif event.key == pygame.K_DOWN and snake.direction != "up":
                    snake.direction = "down"
                elif event.key == pygame.K_LEFT and snake.direction != "right":
                    snake.direction = "left"
                elif event.key == pygame.K_RIGHT and snake.direction != "left":
                    snake.direction = "right"

        # 移动蛇
        snake.move()
        # 判断是否吃到食物
        if snake.body[0] == food.block:
            snake.grow()
            food.block = food.generate_block()

            # 根据得分调整速度
            if speed < max_speed:
                speed += 2

            # 判断是否超过历史最高分，并更新它
            if snake.score > snake.high_score:
                snake.high_score = snake.score


        # 判断是否撞墙或自己
        if (snake.body[0][0] < 0 or snake.body[0][1] >= width or
                snake.body[0][1] < 0 or snake.body[0][1] >= height or
                snake.body[0] in snake.body[1:]):
            game_over = True



        # 绘制游戏界面
        screen.fill(black)
        snake.draw()
        food.draw()
        pygame.display.update()

        # 控制游戏速度
        clock.tick(speed)

    # 在游戏结束时显示得分和历史最高分
    font = pygame.font.Font(None, 50)
    text1 = font.render("Game Over - Score: {}".format(snake.score), True, white)
    text_rect1 = text1.get_rect(center=(width // 2, height // 2 - 50))
    screen.blit(text1, text_rect1)

    text2 = font.render("High Score: {}".format(snake.high_score), True, white)
    text_rect2 = text2.get_rect(center=(width // 2, height // 2 + 50))
    screen.blit(text2, text_rect2)

    pygame.display.update()

    # 等待用户按下按键
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                waiting = False

    # 结束 Pygame
    pygame.quit()
