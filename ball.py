import pygame

class Ball():
    
    def __init__(self, screen, image, x, y) -> None:
        self.screen = screen
        self.image = image
        self.ball_rect = self.image.get_rect(x = x, y = y)
        self.velocity = 1
        self.velocity_x = self.velocity
        self.velocity_y = self.velocity
        self.is_collide = False
        
    def draw_ball(self):
        self.screen.blit(self.image, (self.ball_rect.x, self.ball_rect.y))
        
    def move_ball(self, paddle):
        self.ball_rect.x += self.velocity_x
        self.ball_rect.y += self.velocity_y
        self.check_bound(paddle)
        
    def check_bound(self, paddle):
        if self.is_collide:
            self.ball_rect.bottom = paddle.paddle_rect.top
            self.velocity_y *= -1
            self.set_collide(False)
        
        if self.ball_rect.x >= self.screen.get_width() - self.ball_rect.w:
            self.ball_rect.x = self.screen.get_width() - self.ball_rect.w
            self.velocity_x *= -1
            
        if self.ball_rect.x <= 0:
            self.ball_rect.x = 0
            self.velocity_x *= -1
            
        # if self.ball_rect.y >= self.screen.get_height() - self.ball_rect.h:
        #     self.ball_rect.y = self.screen.get_height() - self.ball_rect.h
        #     self.velocity_y *= -1
            
        if self.ball_rect.y <= 0:
            self.ball_rect.y = 0
            self.velocity_y *= -1
            
    def set_collide(self, new):
        self.is_collide = new
        
    def set_col_block(self):
        self.velocity_y *= -1