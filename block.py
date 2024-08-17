import pygame

class Block():
    
    def __init__(self, screen, image, x, y):
        self.screen = screen
        self.block_image = image
        self.block_rect = self.block_image.get_rect(x = x, y = y)
        
    def draw_block(self):
        self.screen.blit(self.block_image, (self.block_rect.x , self.block_rect.y))