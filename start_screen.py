import setting
import pygame


def start_screen():
    title_font = pygame.font.Font(None, 80)
    text_font = pygame.font.Font(None, 40)
    title_text = title_font.render("Snake Game", True, white)
    title_rect = title_text.get_rect(center=(width // 2, height // 3))

    instruction_text = text_font.render("Press any key to start", True, white)
    instruction_rect = instruction_text.get_rect(center=(width // 2, height // 2))

    screen.fill(black)
    screen.blit(title_text, title_rect)
    screen.blit(instruction_text, instruction_rect)
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