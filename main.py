import pygame
pygame.init()
win = pygame.display.set_mode((1000, 500))
color = (255, 255, 255)
win.fill(color)
pygame.display.flip()
pygame.display.set_caption("First Game")

#initial values needed for motion
x = 50
y = 50
width = 40
height = 60
vel = 5
run = True

while run:
    pygame.time.delay(100) # This will delay the game the given amount of milliseconds. In our casee 0.1 seconds will be the delay

    for event in pygame.event.get():  # This will loop through a list of any keyboard or mouse events.
        if event.type == pygame.QUIT: # Checks if the red button in the corner of the window is clicked
            run = False  # Ends the game loop

pygame.quit()  
