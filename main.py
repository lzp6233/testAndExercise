import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Set up game window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
BLOCK_SIZE = 20
game_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Snake Game')

# Define directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

class Snake:
    def __init__(self):
        self.length = 1
        self.positions = [(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.color = GREEN
        self.score = 0

    def get_head_position(self):
        return self.positions[0]

    def turn(self, new_direction):
        if len(self.positions) > 1 and (new_direction[0] * -1, new_direction[1] * -1) == self.direction:
            return
        else:
            self.direction = new_direction

    def move(self):
        cur = self.get_head_position()
        x = cur[0] + self.direction[0] * BLOCK_SIZE
        y = cur[1] + self.direction[1] * BLOCK_SIZE
        new_position = (x, y)
        self.positions.insert(0, new_position)
        if len(self.positions) > self.length:
            self.positions.pop()

    def eat_food(self):
        self.length += 1
        self.score += 1

    def check_collision(self):
        head = self.get_head_position()
        return (
            head[0] < 0 or head[0] >= WINDOW_WIDTH or
            head[1] < 0 or head[1] >= WINDOW_HEIGHT or
            head in self.positions[1:]
        )

def generate_food(snake_positions):
    while True:
        position = (random.randint(0, (WINDOW_WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE,
                    random.randint(0, (WINDOW_HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE)
        if position not in snake_positions:
            return position

def draw_objects(snake, food_position):
    game_window.fill(BLACK)
    for position in snake.positions:
        pygame.draw.rect(game_window, GREEN, pygame.Rect(position[0], position[1], BLOCK_SIZE - 2, BLOCK_SIZE - 2))
    pygame.draw.rect(game_window, RED, pygame.Rect(food_position[0], food_position[1], BLOCK_SIZE - 2, BLOCK_SIZE - 2))
    pygame.display.flip()

def quit_game():
    pygame.quit()
    sys.exit(0)

def main_game():
    snake = Snake()
    food_position = generate_food(snake.positions)
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
            elif event.type == pygame.KEYDOWN:
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

        snake.move()
        
        if snake.get_head_position() == food_position:
            snake.eat_food()
            food_position = generate_food(snake.positions)

        if snake.check_collision():
            break

        draw_objects(snake, food_position)
        clock.tick(10)

    return snake.score

def show_start_screen():
    game_window.fill(BLACK)
    font = pygame.font.Font(None, 74)
    title = font.render('Snake Game', True, WHITE)
    prompt = pygame.font.Font(None, 36).render('Press SPACE to start, Q to quit', True, WHITE)
    
    game_window.blit(title, (WINDOW_WIDTH // 2 - title.get_width() // 2, WINDOW_HEIGHT // 3))
    game_window.blit(prompt, (WINDOW_WIDTH // 2 - prompt.get_width() // 2, WINDOW_HEIGHT // 2))
    pygame.display.flip()

def show_game_over(score):
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
        show_start_screen()
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit_game()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        waiting = False
                    elif event.key == pygame.K_q:
                        quit_game()
        
        score = main_game()
        show_game_over(score)
        
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit_game()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        waiting = False
                    elif event.key == pygame.K_q:
                        quit_game()
