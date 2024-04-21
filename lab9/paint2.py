import pygame

pygame.init() # Initialize pygame

painting = []

timer = pygame.time.Clock() # We need it for future use with fps

fps = 60 # Set Frames per second

activeColor = (0, 0, 0)
activeShape = 0

w = 800 # Set Window Size
h = 600

screen = pygame.display.set_mode([w, h]) # Set Screen

pygame.display.set_caption("Paint") # Set Window Title

def drawDisplay():
    pygame.draw.rect(screen, 'gray', [0, 0, w, 50]) # Draw Display
    pygame.draw.line(screen, 'black', [0, 50], [w, 50]) # Draw Line separator
    shapes = []
    rect = pygame.draw.rect(screen, 'black', [5, 5, 40, 40])  # Rectangle
    shapes.append([rect, 0])
    circle = pygame.draw.circle(screen, 'black', [70, 25], 20)  # Circle
    shapes.append([circle, 1])
    equilateral_triangle = pygame.draw.polygon(screen, 'black', [[92, 5], [120, 40], [148, 5]])  # Right Triangle
    shapes.append([equilateral_triangle, 2])
    right_triangle = pygame.draw.polygon(screen, 'black', [[140, 40], [170, 40], [170, 5]])  # Equilateral Triangle
    shapes.append([right_triangle, 3])
    rhombus = pygame.draw.polygon(screen, 'black', [[180, 25], [215, 5], [250, 25], [215, 45]])  # Rhombus
    shapes.append([rhombus, 4])
    
    colors=[]
    blue = [pygame.draw.rect(screen, (0, 0, 255), [w - 35, 10, 20, 20]), (0, 0, 255)] # Draw colors
    colors.append(blue)
    red = [pygame.draw.rect(screen, (255, 0, 0), [w - 70, 10, 20, 20]), (255, 0, 0)] # Draw colors
    colors.append(red)
    green = [pygame.draw.rect(screen, (0, 255, 0), [w - 105, 10, 20, 20]), (0, 255, 0)] # Draw colors
    colors.append(green)
    yellow = [pygame.draw.rect(screen, (255, 255, 0), [w - 140, 10, 20, 20]), (255, 255, 0)] # Draw colors
    colors.append(yellow)
    black = [pygame.draw.rect(screen, (0, 0, 0), [w - 175, 10, 20, 20]), (0, 0, 0)] # Draw colors
    colors.append(black)
    purple = [pygame.draw.rect(screen, (255, 0, 255), [w - 205, 10, 20, 20]), (255, 0, 255)] # Draw colors
    colors.append(purple)
    eraser = [pygame.draw.rect(screen, (255, 255, 255), [w - 240, 10, 20, 20]), (255, 255, 255)] # Draw Eraser
    colors.append(eraser)
    return colors,shapes


def drawPaint(paints):
    for paint in paints:
        if paint[2] == 1:
            pygame.draw.circle(screen, paint[0], paint[1], 15)
        elif paint[2] == 0:
            pygame.draw.rect(screen, paint[0], [paint[1][0]-30, paint[1][1]-30, 60, 60])
        elif paint[2] == 2:
            pygame.draw.polygon(screen, paint[0], [[paint[1][0], paint[1][1]+15], [paint[1][0]-15, paint[1][1]-15], [paint[1][0]+15, paint[1][1]-15]])
        elif paint[2] == 3:
            pygame.draw.polygon(screen, paint[0], [[paint[1][0]+15, paint[1][1]+15], [paint[1][0]-15, paint[1][1]+15], [paint[1][0]+15, paint[1][1]-15]])
        elif paint[2] == 4:
            pygame.draw.polygon(screen, paint[0], [[paint[1][0], paint[1][1]-20], [paint[1][0]+40, paint[1][1]], [paint[1][0], paint[1][1]+20], [paint[1][0]-40, paint[1][1]]])

def draw():
    global activeColor, activeShape, mouse
    if mouse[1] > 100:
        if activeShape == 0:
            pygame.draw.rect(screen, activeColor, [mouse[0]-15, mouse[1]-15, 30, 30])
        elif activeShape == 1:
            pygame.draw.circle(screen, activeColor, mouse, 15)
        elif activeShape == 2:
            pygame.draw.polygon(screen, activeColor, [[mouse[0], mouse[1]+15], [mouse[0]-15, mouse[1]-15], [mouse[0]+15, mouse[1]-15]])
        elif activeShape == 3:
            pygame.draw.polygon(screen, activeColor, [[mouse[0]+15, mouse[1]+15], [mouse[0]-15, mouse[1]+15], [mouse[0]+15, mouse[1]-15]])
        elif activeShape == 4:
            pygame.draw.polygon(screen, activeColor, [[mouse[0], mouse[1]-20], [mouse[0]+40, mouse[1]], [mouse[0], mouse[1]+20], [mouse[0]-40, mouse[1]]])

run = True
while run:
    timer.tick(fps) # Set FPS
    screen.fill('white') # Fill Screen
    colors,shapes=drawDisplay()
    mouse = pygame.mouse.get_pos() # Get Mouse Position
    draw()
    
    click = pygame.mouse.get_pressed()[0] # Get Mouse Button Pressed
    if click and mouse[1] > 100:
        painting.append((activeColor, mouse, activeShape)) # Add Mouse Position to List
    drawPaint(painting)

    for event in pygame.event.get(): # Set quit event
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN: # Set quit event
            if event.key == pygame.K_ESCAPE:
                run = False

        if event.type == pygame.KEYDOWN: # Set quit event
            if event.key == pygame.K_SPACE:
                painting = []

        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in colors:
                if i[0].collidepoint(event.pos):
                    activeColor = i[1]
            for i in shapes:
                if i[0].collidepoint(event.pos):
                    activeShape = i[1]
    

    pygame.display.flip() # Update Screen