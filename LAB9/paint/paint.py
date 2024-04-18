import pygame

pygame.init() # Initialize pygame

paintings = []

timer = pygame.time.Clock() # We need it for future use with fps

fps = 60 # Set Frames per second

active_color = (0, 0, 0)
active_shape = 0

window_width = 800 # Set Window Width
window_height = 600 # Set Window Height

screen = pygame.display.set_mode([window_width, window_height]) # Set Screen

pygame.display.set_caption("Drawing App") # Set Window Title

def draw_display():
    pygame.draw.rect(screen, 'gray', [0, 0, window_width, 100]) # Draw Display
    pygame.draw.line(screen, 'black', [0, 100], [window_width, 100]) # Draw Line separator
    rect_button = [pygame.draw.rect(screen, 'black', [10, 10, 80, 80]), 0]
    circle_button = [pygame.draw.rect(screen, 'black', [100, 10, 80, 80]), 1]
    triangle_button = [pygame.draw.rect(screen, 'black', [200, 10, 80, 80]), 2]
    rhombus_button = [pygame.draw.rect(screen, 'black', [300, 10, 80, 80]), 3]
    pygame.draw.rect(screen, 'white', [20, 20, 60, 60])
    pygame.draw.circle(screen, 'white', [140, 50], 30)
    pygame.draw.polygon(screen, 'white', ((270, 75), (210, 75), (239, 20)))
    pygame.draw.polygon(screen, 'white', ((340, 20), (370, 50), (340, 80), (310, 50)))

    blue_button = [pygame.draw.rect(screen, (0, 0, 255), [window_width - 35, 10, 25, 25]), (0, 0, 255)] # Draw colors
    red_button = [pygame.draw.rect(screen, (255, 0, 0), [window_width - 35, 35, 25, 25]), (255, 0, 0)] # Draw colors
    green_button = [pygame.draw.rect(screen, (0, 255, 0), [window_width - 60, 10, 25, 25]), (0, 255, 0)] # Draw colors
    yellow_button = [pygame.draw.rect(screen, (255, 255, 0), [window_width - 60, 35, 25, 25]), (255, 255, 0)] # Draw colors
    black_button = [pygame.draw.rect(screen, (0, 0, 0), [window_width - 85, 10, 25, 25]), (0, 0, 0)] # Draw colors
    purple_button = [pygame.draw.rect(screen, (255, 0, 255), [window_width - 85, 35, 25, 25]), (255, 0, 255)] # Draw colors
    eraser_button = [pygame.draw.rect(screen, (255, 255, 255), [window_width - 150, 20, 25, 25]), (255, 255, 255)] # Draw Eraser
    return [blue_button, red_button, green_button, yellow_button, black_button, purple_button, eraser_button], [rect_button, circle_button, triangle_button, rhombus_button]

def draw_paintings(paints):
    for paint in paints:
        if paint[2] == 1:
            pygame.draw.circle(screen, paint[0], paint[1], 15) # Draw Paint
        if paint[2] == 0:
            pygame.draw.rect(screen, paint[0], [paint[1][0]-15, paint[1][1]-15, 30, 30]) # Draw Paint
        if paint[2] == 2:
            pygame.draw.polygon(screen, paint[0], ((paint[1][0]-10, paint[1][1]+10), (paint[1][0], paint[1][1]-10), (paint[1][0]+10, paint[1][1]+10)))
        if paint[2] ==3:
            pygame.draw.polygon(screen, paint[0], ((paint[1][0], paint[1][1]-10), (paint[1][0]+10, paint[1][1]), (paint[1][0], paint[1][1]+10), (paint[1][0]-10, paint[1][1])))

def draw():
    global active_color, active_shape, mouse_pos
    if mouse_pos[1] > 100:
        if active_shape == 0:
            pygame.draw.rect(screen, active_color, [mouse_pos[0]-15, mouse_pos[1]-15, 30, 30]) # Draw
        if active_shape == 1:
            pygame.draw.circle(screen, active_color, mouse_pos, 15)
        if active_shape == 2:
            pygame.draw.polygon(screen, active_color, ((mouse_pos[0]-10, mouse_pos[1]+10), (mouse_pos[0], mouse_pos[1]-10), (mouse_pos[0]+10, mouse_pos[1]+10)))
        if active_shape == 3:
            pygame.draw.polygon(screen, active_color, ((mouse_pos[0], mouse_pos[1]-10), (mouse_pos[0]+10, mouse_pos[1]), (mouse_pos[0],mouse_pos[1]+10 ), (mouse_pos[0]-10, mouse_pos[1])))

run = True
while run:
    timer.tick(fps) # Set FPS
    screen.fill('white') # Fill Screen
    colors, shapes = draw_display() # Draw Display

    mouse_pos = pygame.mouse.get_pos() # Get Mouse Position
    draw()
    
    click = pygame.mouse.get_pressed()[0] # Get Mouse Button Pressed
    if click and mouse_pos[1] > 100:
        paintings.append((active_color, mouse_pos, active_shape)) # Add Mouse Position to List
    draw_paintings(paintings)

    for event in pygame.event.get(): # Set quit event
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN: # Set quit event
            if event.key == pygame.K_ESCAPE:
                run = False

        if event.type == pygame.KEYDOWN: # Set quit event
            if event.key == pygame.K_SPACE:
                paintings = []

        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in colors:
                if i[0].collidepoint(event.pos):
                    active_color = i[1]
            for i in shapes:
                if i[0].collidepoint(event.pos):
                    active_shape = i[1]
    
    pygame.display.flip() # Update Screen
