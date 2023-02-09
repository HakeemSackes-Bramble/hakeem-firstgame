import pygame
pygame.init()
win = pygame.display.set_mode((500, 500))
color = (255, 255, 255)
win.fill(color)
pygame.display.flip()
pygame.display.set_caption("First Game")

isLeft = False
isRight = False
isUp = False
isDown = False

x = 50
y = 50
width = 40
height = 40
vel = 5
run = True

while run:
    pygame.time.delay(100) 

    for event in pygame.event.get():  
        if event.type == pygame.QUIT:
            run = False 
        if event.type == pygame.KEYDOWN:
            if event.type == pygame.K_LEFT:
                isLeft = True
            if event.type == pygame.K_RIGHT:
                isRight = True
            if event.type == pygame.K_UP:
                isUp = True
            if event.type == pygame.K_DOWN:
                isDown = True    
        if event.type == pygame.KEYUP:
            if event.type == pygame.K_LEFT:
                isLeft = False
            if event.type == pygame.K_RIGHT:
                isRight = False
            if event.type == pygame.K_UP:
                isUp = False
            if event.type == pygame.K_DOWN:
                isDown = False        
        if isLeft:
            x -= vel
        if isRight:
            x += vel
        if isUp:
            y -= vel
        if isDown:
            y += vel 
    pygame.draw.rect(win, (255,0,0), (x, y, width, height))   
    pygame.display.update() 
  
pygame.quit()  
