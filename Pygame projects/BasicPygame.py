import pygame


def block_display():
    """
    displays a basic blue box that bounces on a black screen 

    """
    size = (500, 500)
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    surface = pygame.Surface((20, 25)) #creates blue box
    surface.fill((0, 20, 100))#fills it with color
    coord, speed = (10, 20), (0, 3) #initial coordinates for display and rate of change of coordinates per display
    running = True
    change_move = 0
    move_lat = False #is true when the box is moving laterally, false otherwise
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False # to end the loop
        screen.fill((0, 0, 0)) #resets by painting screen black
        screen.blit(surface, coord) #paints box on the screen with top left at coordinates coord
        if (coord[1] + surface.get_height()) > screen.get_height(): #if box reaches bottom end of screen
            change_move += 1
            speed = (0, -3) 
        elif (coord[1] + speed[1]) < 0: #if box reaches top end of screen
            change_move += 1
            speed = (0, 3)
        elif (coord[0] + surface.get_width()) > screen.get_width(): #if box reaches right end of the screen
            change_move += 1
            speed = (-3, 0)
        elif coord[0] + speed[0] < 0: # if box reaches left end of the screen
            change_move += 1
            speed = (3, 0)
        if change_move == 2:
            change_move = 0
            move_lat = not move_lat
            if move_lat:
                speed = (3, 0)
            else:
                speed = (0, 3)
        coord = (coord[0] + speed[0], coord[1] + speed[1])
        pygame.display.flip()
        clock.tick(60)

def text_display():
    pygame.font.init()
    my_font = pygame.font.SysFont("Comic Sans MS", 26, True)
    size = (500, 600)
    screen = pygame.display.set_mode(size)
    txt_color = (255, 255, 255) #white
    txt_surf = my_font.render("Welcome", False, txt_color)
    coord = (10, 200)
    screen.blit(txt_surf, coord)
    pygame.display.flip()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False





if __name__ == "__main__":
    pygame.init()
    block_display()
    text_display()