import pygame
import random

class SnakeGame:
    def __init__(self):
        pygame.init()

        #           COLORS
        self.bg = (150, 150, 150)  # Background 
        self.h = (255, 150, 20)  # Head 
        self.body = (0, 200, 255)  # Body 
        self.fo = (200, 10, 10)  # Food 
        self.sc = (255, 150, 20)  # Score 
        self.red = (213, 50, 80)  # Game over message 
        self.outer = (100, 100, 200)  # Snake outer 

        #         SIZE DISPLAY
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

        #               FONTS
        self.font_style = pygame.font.SysFont("bahnschrift", 25)
        self.score_font = pygame.font.SysFont("freesans", 35)


