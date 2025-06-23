import pygame
from config import WIDTH, HEIGHT, BLACK, GREEN, RED, YELLOW, BG_COLOR, GRID_COLOR, GRID_SIZE, DEFAULT_WIN_SCORE
from snake import Snake, UP, DOWN, LEFT, RIGHT
from food import Food
from snake_ai import SafeSnakeAI

class Game:
    def __init__(self, win_score=DEFAULT_WIN_SCORE, mode='player'):
        pygame.init()
        pygame.font.init()  # Explicitly initialize font module
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Snake Game')
        # Font loading with fallback
        try:
            self.font = pygame.font.SysFont('arial', 24)
        except Exception:
            self.font = pygame.font.Font(None, 24)
        self.clock = pygame.time.Clock()
        self.snake = Snake()
        self.food = Food(self.snake.body)
        self.score = 0
        self.running = True
        self.win_score = win_score
        self.mode = mode  # 'player' or 'ai'
        self.ai = SafeSnakeAI()

    def draw_block(self, color, pos):
        rect = pygame.Rect(pos[0]*GRID_SIZE, pos[1]*GRID_SIZE, GRID_SIZE, GRID_SIZE)
        pygame.draw.rect(self.screen, color, rect)

    def draw_grid(self):
        for x in range(0, WIDTH, GRID_SIZE):
            pygame.draw.line(self.screen, GRID_COLOR, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, GRID_SIZE):
            pygame.draw.line(self.screen, GRID_COLOR, (0, y), (WIDTH, y))

    def draw_score(self):
        mode_str = 'AI' if self.mode == 'ai' else 'Player'
        text = self.font.render(f'Mode: {mode_str}  Score: {self.score} / {self.win_score}', True, (255,255,255))
        self.screen.blit(text, (10, 10))

    def handle_events(self):
        if self.mode == 'player':
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.snake.set_direction(UP)
                    elif event.key == pygame.K_DOWN:
                        self.snake.set_direction(DOWN)
                    elif event.key == pygame.K_LEFT:
                        self.snake.set_direction(LEFT)
                    elif event.key == pygame.K_RIGHT:
                        self.snake.set_direction(RIGHT)
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

    def ai_decide_direction(self):
        new_dir = self.ai.get_direction(self.snake, self.food.position)
        self.snake.set_direction(new_dir)

    def update(self):
        if self.mode == 'ai':
            self.ai_decide_direction()
        self.snake.move()
        if self.snake.body[0] == self.food.position:
            self.snake.grow()
            self.food.respawn(self.snake.body)
            self.score += 1
        if self.snake.hit_wall() or self.snake.hit_self():
            self.show_gameover_dialog(win=False)
            self.running = False
        elif self.score >= self.win_score:
            self.show_gameover_dialog(win=True)
            self.running = False

    def draw(self):
        self.screen.fill(BG_COLOR)
        self.draw_grid()
        self.draw_block(RED, self.food.position)
        # Snake head yellow, body green
        for i, block in enumerate(self.snake.body):
            color = YELLOW if i == 0 else GREEN
            self.draw_block(color, block)
        self.draw_score()
        pygame.display.flip()

    def show_gameover_dialog(self, win=False):
        # Game over popup, restart or quit
        msg = 'You Win!' if win else 'Game Over!'
        import tkinter as tk
        from tkinter import messagebox, simpledialog
        root = tk.Tk()
        root.withdraw()
        res = messagebox.askyesno(msg, f'{msg}\nScore: {self.score}\nRestart?')
        win_score = self.win_score
        if res:
            value = simpledialog.askinteger('Win Score', 'Please enter win score (default 10):', minvalue=1)
            win_score = value if value else self.win_score
        root.destroy()
        if res:
            from config import DEFAULT_WIN_SCORE
            self.__init__(win_score, self.mode)
            self.run()
        else:
            pygame.quit()

    def run(self):
        while self.running:
            self.clock.tick(10)
            self.handle_events()
            self.update()
            self.draw()
        pygame.quit() 