import pygame

pygame.init()
    #screen
screen = pygame.display.set_mode((700,700))
    #colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)
    #variables
x = 350
y = 350
step = 20
radius = 25
clock = pygame.time.Clock()
    #events
done = False
while not done:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    done = True
    #keyboards
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: 
        if y - step >= 25:
            y -= step
        else:
            y = 25 
    elif pressed[pygame.K_DOWN]: 
        if y + step <= 675:
            y += step
        else:
            y = 675
    elif pressed[pygame.K_LEFT]: 
        if x - step >= 25:
            x -= step
        else:
            x = 25
    elif pressed[pygame.K_RIGHT]: 
        if x + step <= 675:
            x += step
        else:
            x = 675
    screen.fill(WHITE)
    pygame.draw.circle(screen, RED, (x,y), radius) #ball

    pygame.display.flip()
    clock.tick(60) #FPS = frame per second(kak v igrah)