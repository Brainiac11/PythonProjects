import pygame
from sys import exit


pygame.init() # Initialize pygame
screen = pygame.display.set_mode((800, 400)) # Create a window
pygame.display.set_caption("Slam Guys") # Set the title of the window
clock = pygame.time.Clock() # Create a clock object
test_surface = pygame.Surface((800, 400)) # Create a surface
test_surface.fill('cyan') # Fill the surface with a color

while True:
    for event in pygame.event.get(): #allows the user to quit the game
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


    screen.blit(test_surface, (0, 0)) # Draw the surface to the screen

    pygame.display.update() #updates the screen
    clock.tick(609) # Set the frame rate to 60 fps
