import pygame as py 
from src.player1 import Player1
from src.player2 import Player2
from src.ball import Ball
import sys
import os

py.init()

# center the window
os.environ['SDL_VIDEO_CENTERED'] = '1'

# variables
widht, height  = 1000, 800
screen = py.display.set_mode([widht,height])
font1 = py.font.Font('fonts/pixel.ttf', 60)
font = py.font.Font('fonts/pixel.ttf', 80)
icon = py.image.load('icon.ico')
clock = py.time.Clock()
score1 = 0 
score2 = 0


ball = Ball(500, 40)

py.display.set_icon(icon)
py.display.set_caption("PyPong")


def menu():
    global screen, widht , height , player1, player2 
    title = font.render("Pong", True, (255,255,255))
    difficultytext = font.render('Difficulty: ', True, (255,255,255))
    wingyttext = font1.render('Maybe try Wingy War?', True, (255,255,255))
    
    hardtext = font1.render('Hard', True, (255,255,255))
    hardtext_rect = hardtext.get_rect(center=(widht/2-10, 400))
    easytext = font1.render('Easy', True, (255,255,255))
    easytext_rect = easytext.get_rect(center=(widht/2-10, 450))
    
    active = True
    
    while active:
        
        screen.fill((0, 0, 0))
        screen.blit(title, (widht/2 - 100, 100))
        screen.blit(hardtext, hardtext_rect)
        screen.blit(easytext, easytext_rect)
        screen.blit(wingyttext, (170, 600))
  
        py.display.update()
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                sys.exit()
            elif event.type == py.MOUSEBUTTONDOWN:
                if hardtext_rect.collidepoint(py.mouse.get_pos()):
                    widht, height = 1000, 800
                    screen = py.display.set_mode((widht, height))
                    os.environ['SDL_VIDEO_CENTERED'] = '1'
                    player1 = Player1(0, height // 2)
                    player2 = Player2(widht - 20, height // 2)
                    active = False
                elif easytext_rect.collidepoint(py.mouse.get_pos()):
                    widht, height = 1000, 400
                    os.environ['SDL_VIDEO_CENTERED'] = '1'
                    player1 = Player1(0, height // 2)
                    player2 = Player2(widht - 20, height // 2) 
                    screen = py.display.set_mode((widht, height))
                    active = False 
    
menu()

score1 = 0
score2 = 0
run= True 
while run:
    for event in py.event.get():
        if event.type == py.QUIT:
            run = False
        
    keys = py.key.get_pressed()
    if keys[py.K_s]:
        player1.down()
    if keys[py.K_w]:
        player1.up()
    if keys[py.K_UP]:
        player2.up()
    if keys[py.K_DOWN]:
        player2.down()     

    
    score1_text = font.render(str(score1) , True , (255,255,255))
    score1_textrect = score1_text.get_rect(center=(50, 50))
    score2_text = font.render(str(score2), True, (255,255,255))
    score2_textrect = score2_text.get_rect(center=(widht - 50, 50))    
    
    ball.move()
    score1, score2 = ball.check_collision(player1, player2, widht, height, score1, score2)
    
    clock.tick(60)    
    screen.fill((0, 0, 0))
    ball.update()
    screen.blit(ball.surf, ball.rect)
    screen.blit(player1.surf, player1.rect)
    screen.blit(player2.surf, player2.rect)
    screen.blit(score1_text, score1_textrect)
    screen.blit(score2_text, score2_textrect)
    py.display.update()

    
py.quit()
sys.exit()