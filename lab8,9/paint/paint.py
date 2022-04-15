import pygame 
 
 
WIDTH, HEIGHT = 1200, 800   # базовый размер окна 
FPS = 120 
draw = False                # нажатие, зажатие - рисуем, отжали - не рисуем  
lastPos = (0, 0)            # базовая позиция  
radius = 8            # базовый радиус для инструментов 
color = 'black'              # базовый цвет 
mode = 'pen'                # базовый режим 
 
pygame.init() 
screen = pygame.display.set_mode([WIDTH, HEIGHT]) 
pygame.display.set_caption('Paint') 
clock = pygame.time.Clock() 
screen.fill(pygame.Color('white')) # закрашиваем в белый цвет, чтобы внутри цикла не обновлялось 
fontRadius = pygame.font.SysFont('Arial', 40, bold=True) 

# (1000,200) till (1000, 500)
Font = pygame.font.Font('freesansbold.ttf', 32)

def buttons_colors(screen, pos, color):
    pygame.draw.rect(screen, color, pos)

def drawLine(screen, start, end, width, color): 
    x1 = start[0] 
    x2 = end[0] 
    y1 = start[1] 
    y2 = end[1] 
     
    dx = abs(x1 - x2) 
    dy = abs(y1 - y2) 
 
    A = y2 - y1 
    B = x1 - x2 
    C = x2 * y1 - x1 * y2 
 
    if dx > dy: 
        if x1 > x2: 
            x1, x2 = x2, x1 
            y1, y2 = y2, y1 
        for x in range(x1, x2): 
            y = (-C - A * x) / B 
            pygame.draw.circle(screen, pygame.Color(color), (x, y), width) 
    else: 
        if y1 > y2: 
            x1, x2 = x2, x1 
            y1, y2 = y2, y1 
        for y in range(y1, y2): 
            x = (-C - B * y) / A 
            pygame.draw.circle(screen, pygame.Color(color), (x, y), width) 
 
 
def drawCircle(screen, start, end, width, color): 
    x1 = start[0] 
    x2 = end[0] 
    y1 = start[1] 
    y2 = end[1] 
    x = (x1 + x2) / 2 
    y = (y1 + y2) / 2 
    radius = abs(x1 - x2) / 2 
    pygame.draw.circle(screen, pygame.Color(color), (x, y), radius, width) 
 
 
def drawRectangle(screen, start, end, width, color): 
    x1 = start[0] 
    x2 = end[0] 
    y1 = start[1] 
    y2 = end[1] 
    widthr = abs(x1 - x2) 
    height = abs(y1 - y2) 
    if x2 > x1 and y2 > y1: 
        pygame.draw.rect(screen, pygame.Color(color), (x1, y1, widthr, height), width) 
    if y2 > y1 and x1 > x2: 
        pygame.draw.rect(screen, pygame.Color(color), (x2, y1, widthr, height), width) 
    if x1 > x2 and y1 > y2: 
        pygame.draw.rect(screen, pygame.Color(color), (x2, y2, widthr, height), width) 
    if x2 > x1 and y1 > y2: 
        pygame.draw.rect(screen, pygame.Color(color), (x1, y2, widthr, height), width) 
     
 
 
def drawSquare(screen, start, end, width, color): 
    x1 = start[0] 
    x2 = end[0] 
    y1 = start[1] 
    y2 = end[1] 
    mn = min(abs(x2 - x1), abs(y2 - y1)) 
 
 
    if x2 > x1 and y2 > y1: 
        pygame.draw.rect(screen, pygame.Color(color), (x1, y1, mn, mn)) 
    if y2 > y1 and x1 > x2: 
        pygame.draw.rect(screen, pygame.Color(color), (x2, y1, mn, mn)) 
    if x1 > x2 and y1 > y2: 
        pygame.draw.rect(screen, pygame.Color(color), (x2, y2, mn, mn)) 
    if x2 > x1 and y1 > y2: 
        pygame.draw.rect(screen, pygame.Color(color), (x1, y2, mn, mn)) 
 
def drawRightTriangle(screen, start, end, width, color): 
    x1 = start[0] 
    x2 = end[0] 
    y1 = start[1] 
    y2 = end[1] 
     
    if x2 > x1 and y2 > y1: 
        pygame.draw.polygon(screen, pygame.Color(color), ((x1, y1), (x2, y2), (x1, y2))) 
    if y2 > y1 and x1 > x2: 
        pygame.draw.polygon(screen, pygame.Color(color), ((x1, y1), (x2, y2), (x1, y2))) 
    if x1 > x2 and y1 > y2: 
        pygame.draw.polygon(screen, pygame.Color(color), ((x1, y1), (x2, y2), (x2, y1))) 
    if x2 > x1 and y1 > y2: 
        pygame.draw.polygon(screen, pygame.Color(color), ((x1, y1), (x2, y2), (x2, y1))) 
 
 
def drawEquilateralTriangle(screen, start, end, width, color): 
    x1 = start[0] 
    x2 = end[0] 
    y1 = start[1] 
    y2 = end[1] 
 
    width_b = abs(x2 - x1) 
    height = (3**0.5) * width_b / 2 
 
    if y2 > y1: 
        pygame.draw.polygon(screen, pygame.Color(color), ((x1, y2), (x2, y2), ((x1 + x2) / 2, y2 - height)), width) 
    else: 
        pygame.draw.polygon(screen, pygame.Color(color), ((x1, y1), (x2, y1), ((x1 + x2) / 2, y1 - height))) 
     
 
def drawRhombus(screen, start, end, width, color): 
    x1 = start[0] 
    x2 = end[0] 
    y1 = start[1] 
    y2 = end[1]
    pygame.draw.lines(screen, pygame.Color(color), True, (((x1 + x2) / 2, y1), (x1, (y1 + y2) / 2), ((x1 + x2) / 2, y2), (x2, (y1 + y2) / 2)), width) 

 
 
while True: 
    # events 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            exit() 
        mouse_position = pygame.mouse.get_pos
         
        # Нажатия на клавиатуру 
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_r: 
                mode = 'rectangle' 
            if event.key == pygame.K_c: 
                mode = 'circle' 
            if event.key == pygame.K_p: 
                mode = 'pen' 
            if event.key == pygame.K_e: 
                mode = 'erase' 
            if event.key == pygame.K_s: 
                mode = 'square' 
            if event.key == pygame.K_q: 
                screen.fill(pygame.Color('white')) 
            if event.key == pygame.K_y: 
                color = 'yellow' 
            if event.key == pygame.K_b: 
                color = 'black' 
            if event.key == pygame.K_g: 
                color = 'gray' 
            if event.key == pygame.K_t: 
                mode = 'right_tri' 
            if event.key == pygame.K_u: 
                mode = 'eq_tri' 
            if event.key == pygame.K_h: 
                mode = 'rhombus' 
            if event.key == pygame.K_UP: 
                radius = min(200, radius + 1)   # ограничение по максимальному размеру радиуса 
            if event.key == pygame.K_DOWN: 
                radius = max(1, radius - 1)     # ограничение по минимальному размеру радиуса 
 
        # Нажатие на мышку 
        if event.type == pygame.MOUSEBUTTONDOWN: 
            draw = True 
            if mode == 'pen': 
                pygame.draw.circle(screen, pygame.Color(color), event.pos, radius) 
            prevPos = event.pos 
 
        # Отпускание мышки 
        if event.type == pygame.MOUSEBUTTONUP:  
            # mouse_position = pygame.mouse.get_pos
            if mode == 'rectangle': 
                drawRectangle(screen, prevPos, event.pos, radius, color)
            elif mode == 'circle': 
                drawCircle(screen, prevPos, event.pos, radius, color) 
            elif mode == 'square': 
                drawSquare(screen, prevPos, event.pos, radius, color) 
            elif mode == 'right_tri': 
                drawRightTriangle(screen, prevPos, event.pos, radius, color) 
            elif mode == 'eq_tri': 
                drawEquilateralTriangle(screen, prevPos, event.pos, radius, color) 
            elif mode == 'rhombus': 
                drawRhombus(screen, prevPos, event.pos, radius, color) 
            # elif red.collidepoint(pygame.mouse.get_pos) == True:
            #     color = (255,0,0)
            draw = False
            

 
        # Перемещение мышки 
        if event.type == pygame.MOUSEMOTION:  
            if draw and mode == 'pen': 
                drawLine(screen, lastPos, event.pos, radius, color) 
            elif draw and mode == 'erase': 
                drawLine(screen, lastPos, event.pos, radius, 'white') 
            lastPos = event.pos 
 
    # show radius & color 
    pygame.draw.rect(screen, pygame.Color(250,250,250), (5, 5, 400, 80)) 
    renderRadius = fontRadius.render(f'{radius}', True, pygame.Color(color)) 
    screen.blit(renderRadius, (5, 5)) 
    pygame.draw.rect(screen, color, (1100, 5, 100, 80))
    if mode == 'rectangle':
        text = Font.render(mode, True, (0,0,0))
        screen.blit(text, (40,10))
    elif mode == 'circle': 
        text = Font.render(mode, True, (0,0,0))
        screen.blit(text, (40,10))        
    elif mode == 'square': 
        text = Font.render(mode, True, (0,0,0))
        screen.blit(text, (40,10))
    elif mode == 'right_tri': 
        text = Font.render(mode, True, (0,0,0))
        screen.blit(text, (40,10))
    elif mode == 'eq_tri': 
        text = Font.render(mode, True, (0,0,0))
        screen.blit(text, (40,10))
    elif mode == 'rhombus': 
        text = Font.render(mode, True, (0,0,0))
        screen.blit(text, (40,10))
    elif mode == 'pen': 
        text = Font.render(mode, True, (0,0,0))
        screen.blit(text, (40,10))


    # display 
    pygame.display.flip() 
    clock.tick(FPS)