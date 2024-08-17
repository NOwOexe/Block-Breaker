import pygame
from paddle import *
from ball import *
from block import *

class Game():
    
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("BlockBreaker")
        self.background = pygame.image.load("images/bg.jpeg")
        self.background = pygame.transform.scale(self.background, (800, 600))
        
        #Paddle
        self.paddle_img = pygame.image.load("images/paddle.png")
        self.paddle_img = pygame.transform.scale(self.paddle_img, (self.paddle_img.get_width() * 2, self.paddle_img.get_height() * 2))
        
        center_img = (self.screen.get_width() - self.paddle_img.get_width()) // 2
        self.paddle = Paddle(self.screen, self.paddle_img, center_img, 500)
        
        #Ball
        self.ball_img = pygame.image.load("images/ball.png").convert_alpha()
        self.ball_img = pygame.transform.scale(self.ball_img, (self.ball_img.get_width() * 2, self.ball_img.get_height() * 2))
        
        center_img2 = (self.screen.get_width() - self.ball_img.get_width()) // 2
        self.ball = Ball(self.screen, self.ball_img, center_img2, 375)
        
        #Block
        self.block_img = pygame.image.load("images/pink_block.png").convert_alpha()
        self.block_img = pygame.transform.scale(self.block_img, (self.block_img.get_width() * 2, self.block_img.get_height() * 2))
        
        self.block_list = []
        for y in self.block_y_pos():
            for x in self.block_x_pos():
                self.block_list.append(Block(self.screen, self.block_img, x, y))
        
        self.clock = pygame.time.Clock()
        
    def block_x_pos(self):
        block_w = self.block_img.get_width()
        gap = 20
        total_block = self.screen.get_width() // (block_w + gap)
        slide_gab = (self.screen.get_width() - ((block_w + gap) * total_block) + gap) // 2
        lst = []
        for x in range(total_block):
            lst.append(slide_gab + (gap + block_w) * x)
        return lst
    
    def block_y_pos(self):
        block_h = self.block_img.get_height()
        row = 5
        gap = 10
        lst = []
        for y in range(row):
            lst.append(gap + (gap + block_h) * y)
        return lst
        
    def run(self):  
        run = True
        while run:
            
            self.delta_time = self.clock.tick(120) / 1000
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                
            self.screen.blit(self.background, (0, 0))
            self.paddle.draw_paddle()
            self.paddle.move_paddle(self.delta_time)
            self.ball.draw_ball()
            self.ball.move_ball(self.paddle)
            self.check_col()
            for block in self.block_list:
                block.draw_block()
            pygame.display.update()
            
        pygame.quit()
        
    def check_col(self):
        if self.paddle.paddle_rect.colliderect(self.ball.ball_rect):
            self.ball.set_collide(True)
        for block in self.block_list:
            if block.block_rect.colliderect(self.ball.ball_rect):
                self.ball.set_col_block()
                self.block_list.remove(block)
        
if __name__ == "__main__":
    game = Game()
    game.run()