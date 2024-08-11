import pygame

class Paddle():
    
    def __init__(self, screen, image, x, y):
        self.screen = screen
        self.image = image
        self.paddle_rect = self.image.get_rect(x = x, y = y)
        self.velocity = 400
    
    def draw_paddle(self):
        self.screen.blit(self.image, (self.paddle_rect.x, self.paddle_rect.y))
        
    def move_paddle(self, delta_time):
        
        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            self.paddle_rect.x = self.paddle_rect.x - (self.velocity * delta_time)
        if key[pygame.K_d]:
            self.paddle_rect.x = self.paddle_rect.x + (self.velocity * delta_time)
            
        self.check_bound()
            
    def check_bound(self):
        
        if self.paddle_rect.x <= 0:
            self.paddle_rect.x = 0
        if self.paddle_rect.x >= self.screen.get_width() - self.paddle_rect.w:
            self.paddle_rect.x = self.screen.get_width() - self.paddle_rect.w