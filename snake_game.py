import pygame
import random

class SnakeGame:
    def __init__(self):
        pygame.init()

        # COLORS
        self.bg = (150, 150, 150)  # Background 
        self.h = (255, 150, 20)  # Head 
        self.body = (0, 200, 255)  # Body 
        self.fo = (200, 10, 10)  # Food 
        self.sc = (255, 150, 20)  # Score 
        self.red = (213, 50, 80)  # Game over message 
        self.outer = (100, 100, 200)  # Snake outer 

        # SIZE DISPLAY
        self.dis_width = 600
        self.dis_hwidth = 300
        self.dis_height = 400
        self.dis_hheight = 200

        # Initialize 
        self.dis = pygame.display.set_mode((self.dis_width, self.dis_height))
        pygame.display.set_caption('Snake Game by Handsome boy.')

        self.clock = pygame.time.Clock()

        # Define snake properties
        self.snake_block = 10 # Size of 1 block

        self.snake_speed = 5 # frame rate


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

    # Display the score
    def thescore(self, score):
        value = self.score_font.render("Your Score: " + str(score), True, self.sc)
        self.dis.blit(value, [0, 0])

    # Constants
    HALF = 2
    LOOP_INDEFINITELY = -1
    START_LENGTH = 1

    # Function for bgm
    
    def play_sound(sound, loop=LOOP_INDEFINITELY):
        sound.play(loop)
        
    def stop_sound(sound):
        sound.stop()
        
    # MAIN
    def gameLoop(self):
        game_over = False
        game_close = False

        # Game over image
        game_over_img = pygame.image.load("game_over_msg.png").convert_alpha()
        game_over_img = pygame.transform.scale(game_over_img, (self.dis_width, self.dis_height))

        # Position and movement
        x1 = self.dis_width / 2
        y1 = self.dis_height / 2
        x1_change = 0
        y1_change = 0

        snake_List = []
        Length_of_snake = 1

        # Food position
        foodx = self.snake_block * random.randint(0, int(self.dis_width / self.snake_block) - 1)
        foody = self.snake_block * random.randint(0, int(self.dis_height / self.snake_block) - 1)



        while not game_over:
            while game_close:
                # Stop ingame sound and play game over sound
                self.ingame_sound.stop()
                self.game_over_sound.play()

                # Display game over message and image
                self.dis.fill(self.bg)
                self.dis.blit(game_over_img, (0, 0))
                self.message("You Lost! P-Play Again   |   Q-Quit", self.red)
                self.thescore(Length_of_snake - 1)
                pygame.display.update()

                # Event handling for game over
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

            # Event handling for gameplay
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

            # Check if game over
            if x1 >= self.dis_width or x1 < 0 or y1 >= self.dis_height or y1 < 0:
                game_close = True

            # Update position
            x1 += x1_change
            y1 += y1_change

            # Clear the screen
            self.dis.fill(self.bg)

            # Draw food
            pygame.draw.rect(self.dis, self.fo, [foodx, foody, self.snake_block, self.snake_block])

            # Update snake list
            snake_Head = []
            snake_Head.append(x1)
            snake_Head.append(y1)
            snake_List.append(snake_Head)
            if len(snake_List) > Length_of_snake:
                del snake_List[0]

            # Check if snake hits itself
            for x in snake_List[:-1]:
                if x == snake_Head:
                    game_close = True

            # Draw snake and score
            self.our_snake(self.snake_block, snake_List)
            self.thescore(Length_of_snake - 1)

            pygame.display.update()

            # Snake eats the food
            if x1 == foodx and y1 == foody:

                # Play eating sound
                self.eating_sound.play()
                # Increase snake length
                Length_of_snake += 1
                # Generate new position for food
                foodx = self.snake_block * random.randint(0, int(self.dis_width / self.snake_block) - 1)
                foody = self.snake_block * random.randint(0, int(self.dis_height / self.snake_block) - 1)

            # Set frame rate

            self.clock.tick(self.snake_speed)
            
            # ingame sound
            while not game_over:
                while game_close:
                    stop_sound(self.ingame_sound)
                    play_sound(self.game_over_sound)
                    self.dis.fill(self.bg)
                    self.dis.blit(game_over_img, (0, 0))

        pygame.quit()


    # Display a message on the screen
    def message(self, msg, color):
        mesg = self.font_style.render(msg, True, color)
        self.dis.blit(mesg, [self.dis_hwidth - 150, self.dis_hheight + 170])


    # Draw the snake

    def our_snake(self, block, snake_list):
        for x in snake_list:
            pygame.draw.rect(self.dis, self.outer, [x[0], x[1], block, block])
            pygame.draw.rect(self.dis, self.body, [x[0] + 1, x[1] + 1, block - 2, block - 2])


if __name__ == "__main__":
    game = SnakeGame()
    game.gameLoop()
