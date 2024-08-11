import pygame

class Ball():
    
    def __init__(self, screen, image, x, y) -> None:
        self.screen = screen
        self.image = image
        self.ball_rect = self.image.get_rect(x = x, y = y)
        self.velocity = 1
        self.velocity_x = self.velocity
        self.velocity_y = self.velocity
        
    def draw_ball(self):
        self.screen.blit(self.image, (self.ball_rect.x, self.ball_rect.y))
        
    def move_ball(self):
        self.ball_rect.x += self.velocity_x
        self.ball_rect.y += self.velocity_y
        self.check_bound()
        
    def check_bound(self):
        if self.ball_rect.x >= self.screen.get_width() - self.ball_rect.w:
            self.ball_rect.x = self.screen.get_width() - self.ball_rect.w
            self.velocity_x *= -1
            
        if self.ball_rect.x <= 0:
            self.ball_rect.x = 0
            self.velocity_x *= -1
            
            
        if self.ball_rect.y >= self.screen.get_height() - self.ball_rect.h:
            self.ball_rect.y = self.screen.get_height() - self.ball_rect.h
            self.velocity_y *= -1
            
        if self.ball_rect.y <= 0:
            self.ball_rect.y = 0
            self.velocity_y *= -1