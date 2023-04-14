import pygame
import random

# 初始化pygame
pygame.init()

# 游戏区域大小
width = 800
height = 600

# 颜色定义
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# 创建游戏窗口
game_display = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

# 定义蛇和食物
snake_block_size = 10
snake_speed = 15

font_style = pygame.font.SysFont(None, 30)


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    game_display.blit(mesg, [width / 6, height / 3])


def draw_snake(snake_block_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(game_display, black, [x[0], x[1], snake_block_size, snake_block_size])


def game_loop():
    game_over = False
    game_close = False

    # 蛇的初始位置
    x1 = width / 2
    y1 = height / 2

    x1_change = 0
    y1_change = 0

    # 初始长度为1
    snake_List = []
    Length_of_snake = 1

    # 随机产生食物的位置
    foodx = round(random.randrange(0, width - snake_block_size) / 10.0) * 10.0
    foody = round(random.randrange(0, height - snake_block_size) / 10.0) * 10.0

    # 游戏主循环
    while not game_over:

        # 如果游戏结束，则显示游戏结束信息，并等待重启
        while game_close == True:
            game_display.fill(white)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        # 处理方向控制事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block_size
                    x1_change = 0

        # 边界判断
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        # 更新蛇的位置和长度
        x1 += x1_change
        y1 += y1_change
        game_display.fill(white)
        pygame.draw.rect(game_display, red, [foodx, foody, snake_block_size, snake_block_size])

        # 蛇的长度变化
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        draw_snake(snake_block_size, snake_List)
        pygame.display.update()

        # 食物是否被吃掉
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - snake_block_size) / 10.0) * 10.0
            foody = round(random.randrange(0, height - snake_block_size) / 10.0) * 10.0
            Length_of_snake += 1

        #