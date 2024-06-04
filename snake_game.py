import pygame
import random

class SnakeGame:
    def __init__(self):
        pygame.init()

        # COLORS
        self.bg = (150, 150, 150)
        self.h = (255, 150, 20)
        self.body = (0, 200, 255)
        self.fo = (200, 10, 10)
        self.sc = (255, 150, 20)
        self.red = (213, 50, 80)
        self.outer = (100, 100, 200)

        # SIZE DISPLAY
        self.dis_width = 600
        self.dis_height = 400

        # Initialize display
        self.dis = pygame.display.set_mode((self.dis_width, self.dis_height))
        pygame.display.set_caption('Snake Game by Handsome Boy.')

        self.clock = pygame.time.Clock()
        self.snake_block = 10
        self.snake_speed = 5

        # Load sounds
        try:
            self.ingame_sound = pygame.mixer.Sound('ingame_sound.wav')
            self.eating_sound = pygame.mixer.Sound('eating.wav')
            self.game_over_sound = pygame.mixer.Sound('gameOver_sound.wav')
        except pygame.error as e:
            print(f"Failed to load sound files: {e}")
            raise SystemExit(e)

        # FONTS
        self.font_style = pygame.font.SysFont("bahnschrift", 25)
        self.score_font = pygame.font.SysFont("freesans", 35)

        self.game_over_img = pygame.image.load("game_over_msg.png").convert_alpha()
        self.game_over_img = pygame.transform.scale(self.game_over_img, (self.dis_width, self.dis_height))

    def display_score(self, score):
        value = self.score_font.render("Your Score: " + str(score), True, self.sc)
        self.dis.blit(value, [0, 0])

    def draw_snake(self, block, snake_list):
        for x in snake_list:
            pygame.draw.rect(self.dis, self.outer, [x[0], x[1], block, block])
            pygame.draw.rect(self.dis, self.body, [x[0] + 1, x[1] + 1, block - 2, block - 2])

    def display_message(self, msg, color):
        mesg = self.font_style.render(msg, True, color)
        self.dis.blit(mesg, [self.dis_width / 4, self.dis_height / 2])

    def play_sound(self, sound, loop=-1):
        sound.play(loop)

    def stop_sound(self, sound):
        sound.stop()

    def gameLoop(self):
        game_over = False
        game_close = False

        x1 = self.dis_width / 2
        y1 = self.dis_height / 2
        x1_change = 0
        y1_change = 0

        snake_List = []
        Length_of_snake = 1

        foodx = self.snake_block * random.randint(0, self.dis_width / self.snake_block - 1)
        foody = self.snake_block * random.randint(0, self.dis_height / self.snake_block - 1)

        self.play_sound(self.ingame_sound)

        while not game_over:

            while game_close:
                self.stop_sound(self.ingame_sound)
                self.play_sound(self.game_over_sound, 0)

                self.dis.fill(self.bg)
                self.dis.blit(self.game_over_img, (0, 0))
                self.display_message("You Lost! P-Play Again   |   Q-Quit", self.red)
                self.display_score(Length_of_snake - 1)
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        game_over = True
                        game_close = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            game_over = True
                            game_close = False
                        if event.key == pygame.K_p:
                            self.gameLoop()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x1_change = -self.snake_block
                        y1_change = 0
                    elif event.key == pygame.K_RIGHT:
                        x1_change = self.snake_block
                        y1_change = 0
                    elif event.key == pygame.K_UP:
                        y1_change = -self.snake_block
                        x1_change = 0
                    elif event.key == pygame.K_DOWN:
                        y1_change = self.snake_block
                        x1_change = 0

            if x1 >= self.dis_width or x1 < 0 or y1 >= self.dis_height or y1 < 0:
                game_close = True

            x1 += x1_change
            y1 += y1_change
            self.dis.fill(self.bg)
            pygame.draw.rect(self.dis, self.fo, [foodx, foody, self.snake_block, self.snake_block])

            snake_Head = [x1, y1]
            snake_List.append(snake_Head)
            if len(snake_List) > Length_of_snake:
                del snake_List[0]

            for x in snake_List[:-1]:
                if x == snake_Head:
                    game_close = True

            self.draw_snake(self.snake_block, snake_List)
            self.display_score(Length_of_snake - 1)

            pygame.display.update()

            if x1 == foodx and y1 == foody:
                self.play_sound(self.eating_sound, 0)
                Length_of_snake += 1
                foodx = self.snake_block * random.randint(0, self.dis_width / self.snake_block - 1)
                foody = self.snake_block * random.randint(0, self.dis_height / self.snake_block - 1)

            self.clock.tick(self.snake_speed)

        pygame.quit()


if __name__ == "__main__":
    game = SnakeGame()
    game.gameLoop()
