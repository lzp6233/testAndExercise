import pygame
import random
import sys

# 初始化 Pygame
pygame.init()

# 定义颜色常量（RGB 格式）
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# 设置游戏窗口
WINDOW_WIDTH = 800   # 窗口宽度
WINDOW_HEIGHT = 600  # 窗口高度
BLOCK_SIZE = 20      # 蛇身方块大小
game_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))  # 创建游戏窗口
pygame.display.set_caption('Snake Game')  # 设置窗口标题

# 定义方向常量
# 向下为正方向
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

class Snake:
    def __init__(self):
        self.length = 1   # 初始长度
        self.positions = [(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)]  # 初始位置（屏幕中心）
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])  # 随机初始方向
        self.color = GREEN  # 蛇的颜色
        self.score = 0    # 初始分数

    def get_head_position(self):
        # 获取蛇头位置
        return self.positions[0]

    def turn(self, new_direction):
        # 转向，防止180度转向
        if len(self.positions) > 1 and (new_direction[0] * -1, new_direction[1] * -1) == self.direction:
            return
        else:
            self.direction = new_direction

    def move(self):
        # 移动蛇
        cur = self.get_head_position()
        x = cur[0] + self.direction[0] * BLOCK_SIZE  # 计算新的 x 坐标
        y = cur[1] + self.direction[1] * BLOCK_SIZE  # 计算新的 y 坐标
        new_position = (x, y)
        self.positions.insert(0, new_position)  # 在头部插入新位置
        if len(self.positions) > self.length:
            self.positions.pop()  # 如果超过长度则删除尾部

    def eat_food(self):
        # 吃到食物，增加长度和分数
        self.length += 1
        self.score += 1

    def check_collision(self):
        # 检查碰撞
        head = self.get_head_position()
        return (
            head[0] < 0 or head[0] >= WINDOW_WIDTH or  # 撞墙
            head[1] < 0 or head[1] >= WINDOW_HEIGHT or
            head in self.positions[1:]  # 撞到自己
        )

def generate_food(snake_positions):
    # 生成食物位置，确保不与蛇重叠
    while True:
        position = (random.randint(0, (WINDOW_WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE,
                    random.randint(0, (WINDOW_HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE)
        if position not in snake_positions:
            return position

def draw_objects(snake, food_position):
    # 绘制蛇和食物
    game_window.fill(BLACK)  # 清空屏幕
    for position in snake.positions:
        pygame.draw.rect(game_window, GREEN, pygame.Rect(position[0], position[1], BLOCK_SIZE - 2, BLOCK_SIZE - 2))
    pygame.draw.rect(game_window, RED, pygame.Rect(food_position[0], food_position[1], BLOCK_SIZE - 2, BLOCK_SIZE - 2))
    pygame.display.flip()  # 更新显示

def quit_game():
    # 退出游戏
    pygame.quit()
    sys.exit(0)

def main_game():
    # 主游戏循环
    snake = Snake()
    food_position = generate_food(snake.positions)
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
            elif event.type == pygame.KEYDOWN:
                # 处理方向键输入
                if event.key == pygame.K_UP:
                    snake.turn(UP)
                elif event.key == pygame.K_DOWN:
                    snake.turn(DOWN)
                elif event.key == pygame.K_LEFT:
                    snake.turn(LEFT)
                elif event.key == pygame.K_RIGHT:
                    snake.turn(RIGHT)
                elif event.key == pygame.K_q:
                    quit_game()

        snake.move()  # 移动蛇
        
        if snake.get_head_position() == food_position:
            snake.eat_food()  # 吃到食物
            food_position = generate_food(snake.positions)  # 生成新食物

        if snake.check_collision():
            break  # 碰撞检测

        draw_objects(snake, food_position)  # 绘制游戏对象
        clock.tick(10)  # 控制游戏速度

    return snake.score

def show_start_screen():
    # 显示开始界面
    game_window.fill(BLACK)
    font = pygame.font.Font(None, 74)
    title = font.render('Snake Game', True, WHITE)
    prompt = pygame.font.Font(None, 36).render('Press SPACE to start, Q to quit', True, WHITE)
    
    game_window.blit(title, (WINDOW_WIDTH // 2 - title.get_width() // 2, WINDOW_HEIGHT // 3))
    game_window.blit(prompt, (WINDOW_WIDTH // 2 - prompt.get_width() // 2, WINDOW_HEIGHT // 2))
    pygame.display.flip()

def show_game_over(score):
    # 显示游戏结束界面
    game_window.fill(BLACK)
    font = pygame.font.Font(None, 74)
    title = font.render('Game Over', True, WHITE)
    score_display = pygame.font.Font(None, 50).render(f'Score: {score}', True, WHITE)
    prompt = pygame.font.Font(None, 36).render('Press SPACE to restart, Q to quit', True, WHITE)
    
    game_window.blit(title, (WINDOW_WIDTH // 2 - title.get_width() // 2, WINDOW_HEIGHT // 3))
    game_window.blit(score_display, (WINDOW_WIDTH // 2 - score_display.get_width() // 2, WINDOW_HEIGHT // 2))
    game_window.blit(prompt, (WINDOW_WIDTH // 2 - prompt.get_width() // 2, WINDOW_HEIGHT // 1.5))
    pygame.display.flip()

if __name__ == '__main__':
    while True:
        show_start_screen()  # 显示开始界面
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit_game()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        waiting = False  # 开始游戏
                    elif event.key == pygame.K_q:
                        quit_game()  # 退出游戏
        
        score = main_game()  # 运行主游戏
        show_game_over(score)  # 显示游戏结束界面
        
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit_game()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        waiting = False  # 重新开始
                    elif event.key == pygame.K_q:
                        quit_game()  # 退出游戏
