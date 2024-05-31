# Display the score
    def thescore(self, score):
        value = self.score_font.render("Score: " + str(score), True, self.sc)
        self.dis.blit(value, [0, 0])

    # Draw the snake
    def our_snake(self, snake_block, snake_list):
        pygame.draw.rect(self.dis, self.outer, [int(snake_list[-1][0]), int(snake_list[-1][1]), snake_block, snake_block])
        pygame.draw.rect(self.dis, self.h, [int(snake_list[-1][0]), int(snake_list[-1][1]), snake_block - 2, snake_block - 2])
        for x in snake_list[0:-1]:
            pygame.draw.rect(self.dis, self.outer, [int(x[0]), int(x[1]), snake_block, snake_block])
            pygame.draw.rect(self.dis, self.body, [int(x[0]), int(x[1]), snake_block - 2, snake_block - 2])

    # Display messages
    def message(self, msg, color):
        mesg = self.font_style.render(msg, True, color)
        self.dis.blit(mesg, [int(self.dis_width / 6), int(self.dis_height / 3)])