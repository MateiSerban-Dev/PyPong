import pygame as py 

class Player2(py.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.surf = py.Surface((20, 80))
        self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect(topleft=(x,y))
        
    def down(self):
        if self.rect.bottom < 800: 
            self.rect.y += 5
   
    def up(self):
        if self.rect.top > 0:  
            self.rect.y -= 5
        
        