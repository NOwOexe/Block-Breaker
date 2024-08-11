import pygame
from paddle import *
from ball import *

class Game():
    
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("BlockBreaker")
        self.background = pygame.image.load("images/bg.jpeg")
        self.background = pygame.transform.scale(self.background, (800, 600))
        self.paddle_img = pygame.image.load("images/paddle.png")
        self.paddle_img = pygame.transform.scale(self.paddle_img, (self.paddle_img.get_width() * 2, self.paddle_img.get_height() * 2))
        
        center_img = (self.screen.get_width() - self.paddle_img.get_width()) // 2
        self.paddle = Paddle(self.screen, self.paddle_img, center_img, 500)
        
        self.ball_img = pygame.image.load("images/ball.png").convert_alpha()
        self.ball_img = pygame.transform.scale(self.ball_img, (self.ball_img.get_width() * 2, self.ball_img.get_height() * 2))
        
        center_img2 = (self.screen.get_width() - self.ball_img.get_width()) // 2
        self.ball = Ball(self.screen, self.ball_img, center_img2, 375)
        
        self.clock = pygame.time.Clock()
    
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
            self.ball.move_ball()
            pygame.display.update()
            
        pygame.quit()
        
if __name__ == "__main__":
    game = Game()
    game.run()